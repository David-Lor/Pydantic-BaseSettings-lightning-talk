from typing import List, Optional

from pydantic import BaseSettings, BaseModel


class PortsSettings(BaseModel):
	http: int
	mqtt: int


class MySettings(BaseSettings):
    hosts: List[str]
    ports: Optional[PortsSettings]
    
    class Config:
        env_prefix = "APP_"


settings = MySettings()
print("App hosts:", settings.hosts)
