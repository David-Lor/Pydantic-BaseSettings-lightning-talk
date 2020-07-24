"""MongoDB connector, providing custom class to load settings from BaseSettings on init
"""

# # Native # #
from typing import Optional

# # Installed # #
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

# # Package # #
from .settings import mongo_settings

__all__ = ("MongoDB",)


class MongoDB(MongoClient):
    """Custom MongoClient that loads settings from BaseSettings custom class on init"""
    database: Optional[Database]
    collection: Optional[Collection]

    def __init__(self, **kwargs):
        super().__init__(
            host=mongo_settings.host,
            port=mongo_settings.port,
            **kwargs
        )
        self.database = self[settings.database] if settings.database else None
        self.collection = self.database[settings.collection] if self.database and settings.collection else None
