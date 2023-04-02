"""Book DAO"""""
import pymongo
from pymongo.errors import DuplicateKeyError

class BookDAO:
    """Book DAO"""
    collection_name = "books"

    def __init__(self, database):
        self.collection = database[self.collection_name]

    def create(self, book):
        """Create book"""
        try:
            self.collection.create_index([("id", pymongo.ASCENDING)], unique=True)
            self.collection.insert_one(book)
            return book, 201
        except DuplicateKeyError:
            return "Book already exists", 409

    def search(self, query, from_=0, size=10):
        """Search books"""
        db_query = {}
        for key, value in query.items():
            if key == "authors":
                db_query[key] = {"$in": value}
            elif key == "categories":
                db_query[key] = {"$in": value}
            else:
                db_query[key] = value
        result = self.collection.find(db_query, {"_id": 0}).skip(from_).limit(size)
        return list(result)

    def get(self, book_id):
        """Get book"""
        return self.collection.find_one({"id": book_id}, {"_id": 0})

    def update(self, book_id, book):
        """Update book"""
        return  self.collection.update_one({"id": book_id}, {"$set": book})

    def delete(self, book_id):
        """Delete book"""
        return self.collection.delete_one({"id": book_id})
