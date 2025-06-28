#alembic/env.py
from __future__ import with_statement
import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Import your models here
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from extension import db


# Alembic Config object
config = context.config
fileConfig(config.config_file_name)

# Metadata for autogenerate support
target_metadata = db.metadata

# Prevent deletion of DB-only tables
def include_object(object, name, type_, reflected, compare_to):
    print(f"Include object? {name} type={type_} reflected={reflected} compare_to={compare_to}")
    if type_ == "table" and reflected and compare_to is None:
        print(f"Excluding table {name}")
        return False
    return True

def run_migrations_offline():
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        compare_server_default=True,
        include_object=include_object,
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
            include_object=include_object,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
