"""Database factory module."""
import os
from app.dao.mongo.mongodb import MongoDBDAOFactory

databse = {
    "mongodb": MongoDBDAOFactory,
}

class DatabaseFactory:
    """Database factory class."""

    @staticmethod
    def create_database():
        """Create Database."""
        database_type = os.environ.get("DATABASE_IMPL", "mongodb")
        return databse[database_type]()
