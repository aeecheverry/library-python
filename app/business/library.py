"""Library Business"""
import os
import requests
from app.factories.database_factory import DatabaseFactory


class Library:
    """Library Class"""
    def __init__(self):
        self.database = DatabaseFactory.create_database()
        self.book_dao = self.database.create_dao("book_dao")
        self.google_library_url = os.getenv("GOOGLE_LIBRARY_URL")

    def update_book(self, book_id, book):
        """Update book"""
        self.book_dao.update(book_id, book)
        return book

    def create_book(self, book):
        """Create book"""
        self.book_dao.create(book)
        return book

    def search_book(self, query):
        """Search book"""
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
            for item in result:
                item["source"] = source
        return result

    def get_book(self, book_id):
        """Get"""
        result = self.book_dao.get(book_id)
        return result

    def delete_book(self, book_id):
        """Delete"""
        return self.book_dao.delete(book_id)
