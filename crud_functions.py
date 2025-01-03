import sqlite3


def initiate_db(title, description, price):
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL)
    """)

    cursor.execute("""INSERT INTO Products (title, description, price)
    VALUES (?, ?, ?)""", (title, description, price))

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()

    result = cursor.execute("SELECT * FROM Products")
    res = result.fetchall()

    connection.commit()
    connection.close()

    return res

list_products = [('Банан', 'Питательный', 100),('Яблоко', 'Полезное', 200),
                 ('Абрикос', 'Сочный', 300),('Банан', 'Сладкий', 400)]


for args in list_products:
    initiate_db(*args)

print(get_all_products())

# connection = sqlite3.connect("Products.db")
# cursor = connection.cursor()
# cursor.execute('DELETE FROM Users')
# connection.commit()
# connection.close()
