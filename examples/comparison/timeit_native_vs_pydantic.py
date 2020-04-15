"""timeit comparison between using os.getenv vs. using pydantic.BaseSettings
"""

from timeit import timeit


def test_native():
    from os import getenv
    from dotenv import load_dotenv

    load_dotenv()
    host = getenv("APP_HOST")
    port = int(getenv("APP_PORT"))
    start = bool(int(getenv("APP_START")))

    # print(host, port, start)

    assert isinstance(host, str)
    assert isinstance(port, int)
    assert isinstance(start, bool)


def test_pydantic():
    from pydantic import BaseSettings

    class MySettings(BaseSettings):
        host: str
        port: int
        start: bool = True
        class Config:
            env_prefix = "APP_"
            env_file = ".env"
    
    settings = MySettings()

    # print(settings.host, settings.port, settings.start)
    
    assert isinstance(settings.host, str)
    assert isinstance(settings.port, int)
    assert isinstance(settings.start, bool)


def do_comparison(times=10):
    time_native = timeit(test_native, number=times)
    time_pydantic = timeit(test_pydantic, number=times)
    
    print(f"native={time_native}")
    print(f"pydantic={time_pydantic}")
    print(f"winner={'pydantic' if time_pydantic < time_native else 'native'}")
    print(f"difference={abs(time_native - time_pydantic)}")


if __name__ == "__main__":
    do_comparison()
