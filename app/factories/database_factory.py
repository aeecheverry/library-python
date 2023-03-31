"""Database factory module."""
import os
from dao.mongodb import MongoDB


databse = {
    "mongodb": MongoDB,
}

class DatabaseFactory:
    """Database factory class."""
    def create_database(self):
        """Create Database."""
        database_type = os.environ.get("DATABASE_IMPL", "mongodb")
        return databse[database_type]()
