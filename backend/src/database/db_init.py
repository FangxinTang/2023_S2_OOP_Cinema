"""Initialize the database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_for_all import Base



engine = create_engine('postgresql://postgres:postgres@localhost/cinema', echo=True)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)




