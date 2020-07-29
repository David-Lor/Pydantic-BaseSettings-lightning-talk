from pydantic import BaseSettings, Field


class MySettings(BaseSettings):
    # https://www.regexpal.com/96770
    host: str = Field(..., regex="^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
    """Must be a valid IPv4 address"""
    port: int = Field(ge=1, le=65535)
    """Must be a valid port between 1~65535 (inclusive)"""
    database: str = Field(min_length=5)
    """Must be a string with at least 5 characters"""
    
    class Config:
        env_prefix = "APP_"
        env_file = ".env"
        anystr_strip_whitespace = True
        """For all strings, strip leading & trailing whitespaces"""


settings = MySettings()
print("App host:", settings.host)
print("App port:", settings.port)
print("App database:", settings.database)
