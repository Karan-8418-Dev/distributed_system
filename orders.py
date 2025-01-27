import sqlite3


conn = sqlite3.connect('C:/Users/a/OneDrive/Desktop/Tradexa/distributed_system/orders.db')

cursor = conn.cursor()


cursor.execute("SELECT * FROM orders")
columns = [description[0] for description in cursor.description]
print("Columns:", columns)
rows = cursor.fetchall()


for row in rows:
     print(dict(zip(columns, row)))

conn.close()
