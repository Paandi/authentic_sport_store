import sqlite3


class ItemModel:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def find_by_name(cls, name):
        print("inside item class find_by_name function")
        connection = sqlite3.connect("C:\\Users\\dinesh.pandey1\\PycharmProjects\\authentic_sport_store\\data.db")
        cursor = connection.cursor()
        query = "select * from item where name = ? "
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        if row:
            return cls(row[0], row[1])
        return None
