from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine, Integer, String, Column, Text, ForeignKey, DateTime
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


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cost = Column(Integer)


class Purchases(Base):
    __tablename__ = "purchase"
    id = Column(Integer, primary_key=True)
    count = Column(Integer)
    # date = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", backref="purchases")

    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    products = relationship("Product", backref="purchases")


"""def create_user(user, k):
    user = User(email=f"user-{k}@email.com")
    session.add(user)
    session.commit()
    print(f"Пользователь user-{k} зарегестрирован")
    return user


def create_prod(product):
    name = input('Введите название товара: ')
    price = float(input('Введите цену: '))
    product = Product(name=name, cost=price)
    session.add(product)
    session.commit()
    print(f"Товар {product} стоимостью {price} зарегестрирован")
    return product


def purchase(user, product):
    print('Выберете предмет, который вы хотите приобрести.')
    prod = session.query(Product.id, Product.name)  # Запрашиваю сессию для получения списка таваров (id, name)
    all_prod = prod.all()  # Запоминаю кортежи
    for i in all_prod:  # иду по списку товаров и вывожу его номер и наименование
        print(f'Номер товара №{i[0]}, название {i[1]}')
    n = int(input("Введите номер товара для преобретения: "))
    c = int(input("Введите количество товара для преобретения: "))
    buy = Purchases(user_id=User.id, produst_id=n, count=c)
    session.add(buy)
    session.commit()
    return buy
"""

if __name__ == "__main__":
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True,
    )
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    choice = int(input("1 - Start. || 2 - Exit.\nYour choice: "))
    numb = 0
    while choice == 1:
        name = str(input("Input your name: "))
        print("----Регистрация пользователя----\n")
        # create_user(user, k)
        user = User(email=f"{name}_{numb}@email.com")
        session.add(user)
        session.commit()
        print(f"Пользователь {name}_{numb} зарегестрирован")

        print("----Регистрация товара----\n")
        # create_prod(product)
        name_prod = input('Введите название товара: ')
        price = float(input('Введите цену: '))
        product = Product(name=name_prod, cost=price)
        session.add(product)
        session.commit()
        print(f"Товар {product} стоимостью {price} зарегестрирован")

        print("----Регистрация покупки----\n")
        # purchase(user, product)
        print('Выберете предмет, который вы хотите приобрести.')
        prod = session.query(Product.id, Product.name)
        all_prod = prod.all()
        for i in all_prod:
            print(f'Номер товара №{i[0]}, название {i[1]}')
        n = int(input("Введите номер товара для преобретения: "))
        c = int(input("Введите количество товара для преобретения: "))
        buy = Purchases(user_id=user.id, product_id=n, count=c)
        session.add(buy)
        session.commit()

        numb += 1
        i = int(input("Желаете продолжить? 1 - да || 2 - нет"))
        if i == 2:
            break
