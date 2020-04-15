"""Loading settings with os.getenv
"""

from os import getenv
from dotenv import load_dotenv

__all__ = ("HOST", "PORT", "START")

load_dotenv()

HOST = getenv("APP_HOST")
PORT = int(getenv("APP_PORT"))
START = bool(int(getenv("APP_START")))

if __name__ == "__main__":
    print("App host:", HOST)
    print("App port:", PORT)
    print("App start:", START)
