from logging.config import fileConfig

from sqlalchemy import create_engine
from sqlalchemy import pool

from alembic import context
from dotenv import load_dotenv

from app.db.database import DATABASE_URL
from app.db.base import Base

# Load environment variables
load_dotenv()

# Alembic config
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import models so they register with Base.metadata
from app.models.Product import Product
from app.models.ProductCategory import ProductCategory
from app.models.ProductSpecs import ProductSpecs

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = create_engine(
        DATABASE_URL,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

    connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()