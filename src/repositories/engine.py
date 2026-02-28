from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.configs.runtime_config import RuntimeConfig

config = RuntimeConfig.global_config()

engine = create_async_engine(
    config.DATABASE_URL,
    echo=config.ECHO,
    pool_pre_ping=True,
)

AsyncSessionFactory = async_sessionmaker(
    engine,
    expire_on_commit=False,
)