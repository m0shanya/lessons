import sqlite3


def create_product_table(name: str, price: int, count: int, comment: str):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            CREATE TABLE products (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR,
               price INTEGER,
               count INTEGER,
               comment VARCHAR,
               datetime DATETIME
            );
            """,
        )
        session.commit()

def create_product(name: str, price: int, count: int, comment: str):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            f"""
               INSERT INTO products (name, price, count, comment)
               VALUES (?, ?, ?, ?);
               """,
            (name, price, count, comment),
        )
        session.commit()

