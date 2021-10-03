import sqlite3
from flask_restful import Resource, reqparse
from Model.User import UserModel
from os import path


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        required=True,
                        help="name can't be blank"
                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="password can't be blank"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        # check in user table if exist return a msg else add a row
        user = UserModel.find_by_name(data['name'])
        if user:
            return {"message": "user already exists"}
        else:
            connection = sqlite3.connect("C:\\Users\\dinesh.pandey1\\PycharmProjects\\authentic_sport_store\\data.db")
            cursor = connection.cursor()
            query = "insert into user values (Null, ?, ?)"
            result = cursor.execute(query, (data['name'], data['password']))
            connection.commit()
            connection.close()
            return {"message": "user added successfully"}
