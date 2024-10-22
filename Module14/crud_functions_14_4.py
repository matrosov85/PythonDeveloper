import sqlite3

DATABASE = 'database_14_4.db'


def initiate_db():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
          id INTEGER PRIMARY KEY,
          title TEXT NOT NULL,
          description TEXT,
          price INTEGER NOT NULL
        );
    ''')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    products = cursor.execute('SELECT * FROM Products').fetchall()
    connection.commit()
    connection.close()
    return products


def add_product(title, description, price):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO Products (title, description, price) VALUES ("{title}", "{description}", {price})')
    connection.commit()
    connection.close()
