import os
from typing import Self
from dotenv import load_dotenv


load_dotenv()

class DataBase:
    def __init__(self: Self) -> None:
        self.DB_USER: str = os.environ.get('DB_USER', 'postgres')
        self.DB_PASS: str = os.environ.get('DB_PASS', 'postgres')
        self.DB_NAME: str = os.environ.get('DB_NAME', 'postgres')
        self.DB_HOST: str = os.environ.get('DB_HOST', 'localhost')
        self.DB_PORT: str = os.environ.get('DB_PORT', '5432')
        

    @property
    def db_dsn(self: Self):
        return (
            f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@'
            f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )
        


class Settings:
    def __init__(self: Self) -> None:
        self.db = DataBase()



settings = Settings()