# Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов"

import sqlite3


connection = sqlite3.connect('not_telegram_14_1.db')
cursor = connection.cursor()

# Создание таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
      id INTEGER PRIMARY KEY,
      username TEXT NOT NULL,
      email TEXT NOT NULL,
      age INTEGER,
      balance INTEGER NOT NULL
    );
''')

# Заполнение таблицы
for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)',
                   (f'User{i}', f'example{i}@gmail.com', i*10))

# Обновление balance у каждой второй записи
for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = 500 WHERE id = ?', (i,))

# Удаление каждой 3ей записи
for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

# Выборка всех записей, где возраст не равен 60
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age <> 60')
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

connection.commit()
connection.close()
