from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True)
    email = Column(String)


DB_USER = "m0shanya"
DB_PASSWORD = "m0shanya"
DB_NAME = "m0shanya"
DB_ECHO = True

if __name__ == "__main__":
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo = True,
    )
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)