"""Core database lifecycle functions."""

import sqlalchemy as sa
from sqlalchemy import engine, orm

from .. import config as global_config


class DatabaseManager:
    """Manages connections, object mappings, and updates."""

    def __init__(self, db_engine: engine.Engine, schema: str = "public"):
        self.active_sessions = 0
        self.schema = schema
        self.db_engine = db_engine

    def _create_tables(self):
        self.metadata = global_config.MODELS_METADATA
        self.metadata.schema = self.schema
        self.metadata.create_all(self.db_engine)

    def dispose(self):
        self.db_engine.dispose()

    def start_session(self):
        self.session = orm.Session(self.db_engine)
        self.session.execute(sa.text(f"SET search_path TO {self.schema}"))
        self.session.expire_on_commit = True
        self.active_sessions += 1

    def close_session(self):
        self.session.close()
        self.active_sessions -= 1

    def set_schema(self, schema: str) -> None:
        self.schema = schema

    def commit(self):
        try:
            self.session.commit()

        except Exception as e:
            self.session.rollback()
            raise e
