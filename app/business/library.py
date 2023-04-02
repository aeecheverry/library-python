"""Library Business"""
import os
import requests
from app.factories.database_factory import DatabaseFactory
from app.schemas.book_schema import BookSchema

class Library:
    """Library Class"""
    def __init__(self):
        self.database = DatabaseFactory.create_database()
        self.book_dao = self.database.create_dao("book_dao")
        self.google_library_url = os.getenv("GOOGLE_LIBRARY_URL")

    def create_book(self, book):
        """Create book"""
        if "source" in book and book["source"] == "google":
            response = requests.get(self.google_library_url, params={"q": book["id"]}, timeout=5000)
            if response.status_code == 200:
                result = response.json()["items"]
                print("***Google***ß")
                print(result)
                source = "google"
            else:
                source = "db interna"
            for item in result:
                item["source"] = source
            book_schema = BookSchema()
            result = book_schema.load(book)
            self.book_dao.create(result)
        return result

    def search_books(self, query):
        """Search book"""
        if "categories" in query:
            query["categories"] = query["categories"].split(",")
        if "authors" in query:
            query["authors"] = query["authors"].split(",")
        if "publication_date" in query:
            query["publication_date"] = str(query["publication_date"])
        result = self.book_dao.search(query)
        if not result:
            response = requests.get(self.google_library_url, params={"q": query}, timeout=5000)
            if response.status_code == 200:
                result = response.json()["items"]
                source = "google"
            else:
                source = "db interna"
            for item in result:
                item["source"] = source
            self.book_dao.create(result)
        else:
            source = "db interna"
            # for item in result:
            #     item["source"] = source
        return result

    def get_book(self, book_id):
        """Get"""
        result = self.book_dao.get(book_id)
        return result

    def delete_book(self, book_id):
        """Delete"""
        book = self.book_dao.get(book_id)
        if book is None:
            return "Book not found", 404

        result = self.book_dao.delete_one({"_id": book_id})
        if result.deleted_count == 1:
            return {"status": "deleted", "book": book}, 200
        else:
            return "Error deleting book", 500

