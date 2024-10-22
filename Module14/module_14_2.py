# Домашнее задание по теме "Выбор элементов и функции в SQL запросах"

import sqlite3


connection = sqlite3.connect('not_telegram_14_2.db')
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

# Удаление записи с id = 6
cursor.execute('DELETE FROM Users WHERE id = 6')

# Подсчет количества всех пользователей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчет суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)

connection.commit()
connection.close()
