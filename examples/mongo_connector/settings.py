"""Settings loader
"""

# # Native # #
from typing import Optional

# # Installed # #
from pydantic import BaseSettings

__all__ = ("mongo_settings",)


class MongoSettings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 27017
    database: Optional[str]
    collection: Optional[str]

    class Config:
        env_file = ".env"
        env_prefix = "MONGO_"


mongo_settings = MongoSettings()
