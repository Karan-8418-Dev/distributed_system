import sqlite3

conn = sqlite3.connect('C:/Users/a/OneDrive/Desktop/Tradexa/distributed_system/products.db')


cursor = conn.cursor()


cursor.execute("SELECT * FROM products")


rows = cursor.fetchall()


for row in rows:
    print(row)


conn.close()
