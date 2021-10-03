import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from Model.item import ItemModel


class Items(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help=" Each item should have a price value"
                        )

    @jwt_required()
    def get(self, name):

        input_item = ItemModel.find_by_name(name)
        if input_item:
            return {"name": input_item.name, "price": input_item.price}
        else:
            return {"message": "item does not exist"}

    @jwt_required()
    def post(self, name):
        # input_data = request.get_json()

        input_data = Items.parser.parse_args()
        if ItemModel.find_by_name(name):
            return {"message": "Item already Exists"}
        else:
            connection = sqlite3.connect("C:\\Users\\dinesh.pandey1\\PycharmProjects\\authentic_sport_store\\data.db")
            cursor = connection.cursor()
            query = "insert into item values (?,?)"
            cursor.execute(query, (name, input_data['price']))
            connection.commit()
            connection.close()
            return {"message": "item added successfully"}

    @jwt_required()
    def put(self, name):
        input_data = Items.parser.parse_args()
        connection = sqlite3.connect("C:\\Users\\dinesh.pandey1\\PycharmProjects\\authentic_sport_store\\data.db")
        cursor = connection.cursor()
        if ItemModel.find_by_name(name):
            print("updating data ")
            query = "update item set price = ? where name = ?"
            cursor.execute(query, (input_data['price'], name))
            connection.commit()
        else:
            query = "insert into item values (?, ?)"
            cursor.execute(query, (name, input_data['price']))
            connection.commit()

        connection.close()
        return {"message": "items updated successfully"}

    @jwt_required()
    def delete(self, name):
        connection = sqlite3.connect("C:\\Users\\dinesh.pandey1\\PycharmProjects\\authentic_sport_store\\data.db")
        cursor = connection.cursor()
        query = " select * from item where name = ?"
        result = cursor.execute(query, (name, )).fetchone()
        if result:
            query = " delete from item where name = ? "
            cursor.execute(query, (name, ))
            connection  .commit()

        connection.close()
        return {"message": "item deleted"}


class ItemAll(Resource):

    @jwt_required()
    def get(self):
        connection = sqlite3.connect("C:\\Users\\dinesh.pandey1\\PycharmProjects\\authentic_sport_store\\data.db")
        cursor = connection.cursor()
        query = " select * from item "
        result = cursor.execute(query)
        output_data = []
        for row in result:
            output_data.append({'name': row[0], 'price': row[1]})
        connection.close()
        return output_data
