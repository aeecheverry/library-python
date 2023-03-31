"""MongoDB DAO"""

import os
from dao.mongodb.userdao import UserDAO

from pymongo import MongoClient

daoMap = {
    "userdao": UserDAO,
}

class MongoDB:
    """MongoDB DAO"""

    def __init__(self):
        """MongoDB DAO"""
        self.client = MongoClient(os.environ.get("MONGODB_URL", "mongodb://localhost:27017/"))
        self.database = self.client[os.environ.get("MONGODB_DATABASE", "library")]

    def create_dao(self, dao_type):
        """Create DAO"""
        return daoMap[dao_type](self.database)
