import sqlite3

DATABASE = 'database_14_5.db'


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
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
          id INTEGER PRIMARY KEY,
          username TEXT NOT NULL,
          email TEXT NOT NULL,
          age INTEGER NOT NULL,
          balance INTEGER NOT NULL
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


def add_user(username, email, age):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO Users (username, email, age, balance) VALUES ("{username}", "{email}", {age}, 1000)')
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    user = cursor.execute(f'SELECT * FROM Users WHERE username = "{username}"').fetchone()
    connection.commit()
    connection.close()
    if user is None:
        return False
    return True


def add_product(title, description, price):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO Products (title, description, price) VALUES ("{title}", "{description}", {price})')
    connection.commit()
    connection.close()
