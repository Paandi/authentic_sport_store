import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

user_table = "create table if not exists user (id Integer primary key, name string, password string)"
item_table = "create table if not exists item (name string, price float)"

cursor.execute(user_table)
cursor.execute(item_table)


connection.commit()
connection.close()
