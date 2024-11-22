import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users
(id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) "
                   "VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", f"{i * 10}", "1000"))

for i in range(1, 11):
    if i % 2 == 0:
        pass
    else:
        cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))


cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

cursor.execute("SELECT * FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for data in users:
    print(f" Имя: {data[1]} | Почта: {data[2]} | Возраст: {data[3]} | Баланс: {data[4]}")

#добавим условие задачи:

cursor.execute("DELETE FROM Users WHERE id  = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
total1 = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
total2 = cursor.fetchone()[0]

print(total2 / total1)

connection.commit()
connection.close()