"""Initialize the database"""
from sqlalchemy import create_engine



engine = create_engine('postgresql://postgres:postgres@localhost/cinema', echo=True)


# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
