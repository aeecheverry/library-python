"""Library Business"""
import os
import requests
from app.factories.database_factory import DatabaseFactory
from app.schemas.book_schema import BookSchema
from app.business.book_api_helper import google_book, open_library

books_api = {
    "google": google_book,
    "open_library": open_library,
}
class Library:
    """Library Class"""
    def __init__(self):
        self.database = DatabaseFactory.create_database()
        self.book_dao = self.database.create_dao("book_dao")
        self.google_library_url = os.getenv("GOOGLE_LIBRARY_URL")
        self.open_library_url = os.getenv("OPEN_LIBRARY_URL")

    def create_book(self, book):
        """Create book"""
        if book["source"] in books_api:
            result = books_api[book["source"]](self, book["id"])
            if not result:
                return "Book not found", 404
            else:
                result = result[0]
                result["source"] = "db_interna"
                book_schema = BookSchema()
                book = book_schema.load(result)
                result, code = self.book_dao.create(book)
                result.pop('_id', None)
                return result, code
        else:
            return "Source not found", 404

    def search_books(self, query):
        """Search book"""
        if "categories" in query:
            query["categories"] = query["categories"].split(",")
        if "authors" in query:
            query["authors"] = query["authors"].split(",")
        if "publishedDate" in query:
            query["publishedDate"] = str(query["publishedDate"])
        books = self.book_dao.search(query)
        if not books:
            books = books_api["google"](self, query)
            if not books:
                return "Book not found", 404
            else:
                book_schema = BookSchema()
                books = book_schema.load(books, many=True)
        return books, 200

    def get_book(self, book_id):
        """Get"""
        result = self.book_dao.get(book_id)
        return result

    def delete_book(self, book_id):
        """Delete"""
        book = self.book_dao.get(book_id)
        if book is None:
            return "Book not found", 404

        result = self.book_dao.delete(book_id)
        if result.deleted_count == 1:
            return {"status": "deleted", "book": book}, 200
        else:
            return "Error deleting book", 500

