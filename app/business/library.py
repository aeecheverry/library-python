"""Library Business"""
#import os
import requests
#from factories.message_broker_factory import MessageBrokerFactory


class Library:
    """Library Class"""
    def update_book(self, book_id, book):
        """Update book"""
        return book

    def create_book(self, book):
        """Create book"""
        return book

    def list_books(self, _input):
        """List books"""
        requests.get(google_library_url, timeout=5000)
        result = self.book_dao.list()
        return result

    def get_book(self, book_id):
        """Get"""
        result = self.book_dao.get(book_id)
        return result

    def delete_book(self, book_id):
        """Delete"""
        return self.book_dao.delete(book_id)
