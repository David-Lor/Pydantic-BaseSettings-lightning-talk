"""Loading settings with a pydantic.BaseSettings custom class
"""

from pydantic import BaseSettings

__all__ = ("settings",)


class MySettings(BaseSettings):
    host: str
    port: int
    start: bool = True

    class Config:
        env_prefix = "APP_"
        env_file = ".env"


settings = MySettings()

if __name__ == "__main__":
    print("App host:", settings.host)
    print("App port:", settings.port)
    print("App start:", settings.start)
