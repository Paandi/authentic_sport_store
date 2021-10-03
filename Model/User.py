import sqlite3


class UserModel:
    def __init__(self, _id, name, pwd):
        self.id = _id
        self.name = name
        self.pwd = pwd

    @classmethod
    def find_by_name(cls, name):
        try:
            connection = sqlite3.connect("C:\\Users\\dinesh.pandey1\\PycharmProjects\\authentic_sport_store\\data.db")
            cursor = connection.cursor()
            query = "select * from user where name = ?"
            result = cursor.execute(query, (name,))
            row = result.fetchone()
            return row

        except:
            print("Error: Failed to connect with Database")

    @classmethod
    def find_by_id(cls, uid):
        try:
            connection = sqlite3.connect("C:\\Users\\dinesh.pandey1\\PycharmProjects\\authentic_sport_store\\data.db")
            cursor = connection.cursor()
            query = "select * from user where id = ?"
            result = cursor.execute(query, (uid,))
            row = result.fetchone()
            return row

        except:
            print("Error: Failed to connect with Database")

