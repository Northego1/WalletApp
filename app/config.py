import os
from typing import Self
from dotenv import load_dotenv


load_dotenv()

class DataBase:
    def __init__(self: Self) -> None:
        self.DB_USER = os.environ.get('DB_USER', 'postgres')
        self.DB_PASS = os.environ.get('DB_PASS', 'postgres')
        self.DB_NAME = os.environ.get('DB_NAME', 'postgres')
        self.DB_HOST = os.environ.get('DB_HOST', 'localhost')
        self.DB_PORT = os.environ.get('DB_PORT', '5432')

        self.conn_pool = int(os.environ.get('conn_pool', 8))
        self.conn_max_overflow = int(os.environ.get('max_overflow', 2))
        self.conn_timeout = int(os.environ.get('timeout', 30))
        self.conn_recycle = int(os.environ.get('conn_recycle', 1800))

        

    @property
    def dsn(self: Self):
        return (
            f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@'
            f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )
        


class Settings:
    def __init__(self: Self) -> None:
        self.db = DataBase()



settings = Settings()