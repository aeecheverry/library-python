"""Book DAO"""""
from pymongo.errors import DuplicateKeyError

class BookDAO:
    """Book DAO"""
    collection_name = "books"

    def __init__(self, database):
        self.collection = database[self.collection_name]

    def create(self, book):
        """Create book"""
        try:
            result = self.collection.insert_one(book)
        except DuplicateKeyError:
            result = None
        return result

    def search(self, query):
        """Search books"""
        db_query = {}
        for key, value in query.items():
            if key == "authors":
                db_query[key] = {"$in": value}
            elif key == "categories":
                db_query[key] = {"$in": value}
            else:
                db_query[key] = value

        result = self.collection.find(db_query, {"_id": 0})
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
