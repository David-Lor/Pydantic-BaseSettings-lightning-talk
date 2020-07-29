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
        env_file = ".env"


settings = MySettings()
print("App hosts:", settings.hosts)
if settings.ports:
	print("App HTTP port:", settings.ports.http)
	print("App MQTT port:", settings.ports.mqtt)
