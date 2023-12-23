"""Initialize the database"""
from sqlalchemy import create_engine
import sys
import pathlib as pl
sys.path.insert(0, str(pl.Path(__file__).resolve().parent.parent))

from models.base_model import Base


engine = create_engine('postgresql://postgres:postgres@localhost/cinema', echo=True)


Base.metadata.create_all(engine)
