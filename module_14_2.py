import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT ,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (
        f'User{i}',
        f'example{i}@gmail.com',
        f'{10*i}',
        '1000'))

cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 != 0', (500, ))

cursor.execute('DELETE FROM Users WHERE (id - 1) % 3 = 0')

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
print(f'Всего пользователей: {total_users}')

cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()[0]
print(f'Суммарный баланс: {total_balance}')
print(f'Средний баланс (расчёт): {total_balance / total_users}')

cursor.execute('SELECT AVG(balance) FROM Users')
avg_balance = cursor.fetchone()[0]
print(f'Средний баланс (функция AVG): {avg_balance}')

connection.commit()
connection.close()
