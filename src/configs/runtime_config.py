import os
from archipy.configs.base_config import BaseConfig

class RuntimeConfig(BaseConfig):

   
    DATABASE_URL: str = os.getenv(
    "DATABASE_URL", 
)
    ECHO: bool = True  

    @property
    def database_url(self) -> str:
        return self.DATABASE_URL

    @classmethod
    def global_config(cls) -> "RuntimeConfig":
        return cls()
