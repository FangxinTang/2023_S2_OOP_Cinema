"""initialize database"""
from typing import Type
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from backend.src.database.models import Base
from backend.src import constance as global_constance


def check_existence_of_demo_item(session: Session, table: Type[Base]) -> None | Type[Base]:
    """Checks if a demo item exists in the database.
    If it does, returns the model class for the item.
    If it doesn't, returns None"""
    query = session.query(table).where(table.id == global_constance.NIL_UUID)
    result = query.first()
    return result


def populate_dummy_data(session: Session):
    """Populates the database with data."""

    from database.dummy_data import DUMMY_DATA

    for model, data in DUMMY_DATA:
        existing_item = check_existence_of_demo_item(session, model)
        if existing_item is None:
            demo_item = model(**data, id=global_constance.NIL_UUID)
            session.add(demo_item)
        
    try:
        session.commit()
        print("Dummy data populated successfully.")
    except Exception as e:
        session.rollback()
        print(f"An error occured: {e}")
    finally:
        session.close()


def create_tables(engine):
    """create all tables"""
    Base.metadata.create_all(bind=engine)

def init_database():
    """Initializes the database. Create tables and populate dummy data"""
    db_url = 'postgresql://postgres:postgres@localhost/cinema'
    engine = create_engine(db_url, echo=True)
    LocalSession = sessionmaker(bind=engine)
    session = LocalSession()
    try:
        print("Initializing database...")
        create_tables(engine)
        print("Tables created.")
        populate_dummy_data(session=session)
        print("Dummy data populated.")
    except Exception as e:
        session.rollback()
        print(f"An error occured: {e}")
    finally:
        session.close()
