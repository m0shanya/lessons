from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine, Integer, String, Column, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DB_USER = "timofey"
DB_PASSWORD = "timofey"
DB_NAME = "timofey"
DB_ECHO = True

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String)

    products = relationship("Product", back_populates="user")


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cost = Column(Integer)

    user = relationship("User", back_populates="products")


class Purchases(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    count = Column(Integer)
    # date = Column()

    user_0 = relationship("User", back_populates="products")
    products_0 = relationship("Product", back_populates="user")


if __name__ == "__main__":
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True,
    )
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for index in range(5):
        user = User(name=f"user-{index}", email=f"user-{index}@email.com", age=index + 20)
        session.add(user)

    session.commit()
