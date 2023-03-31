"""Book DAO"""""
import os

class BookDAO:
    """Book DAO"""
    collection_name = "books"

    def __init__(self, database):
        self.collection = database[self.collection_name]

    def create(self, book):
        """Create book"""
        return self.collection.insert_one(book)

    def list(self):
        """List books"""
        return self.collection.find()

    def get(self, book_id):
        """Get book"""
        return self.collection.find_one({"id": book_id})

    def update(self, book_id, book):
        """Update book"""
        return  self.collection.update_one({"id": book_id}, {"$set": book})

    def delete(self, book_id):
        """Delete book"""
        return self.collection.delete_one({"id": book_id})
