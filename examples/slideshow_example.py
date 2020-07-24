from pydantic import BaseSettings


class MySettings(BaseSettings):
    host: str
    port: int
    start: bool = True

    class Config:
        env_prefix = "APP_"
        env_file = ".env"


settings = MySettings()
print("App host:", settings.host)
print("App port:", settings.port)
print("App start:", settings.start)
