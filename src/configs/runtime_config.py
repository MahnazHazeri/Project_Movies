import os
from dotenv import load_dotenv
from archipy.configs.base_config import BaseConfig

load_dotenv()


class RuntimeConfig(BaseConfig):

    DATABASE_URL: str = os.getenv("DATABASE_URL")
    ECHO: bool = os.getenv("ECHO", "False").lower() == "true"

    @classmethod
    def global_config(cls):
        return cls()