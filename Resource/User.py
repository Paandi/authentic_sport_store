from flask_restful import Resource, reqparse
from Model.User import UserModel


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

        if UserModel.find_by_name(data['name']):
            return {"message": "user already exists"}
        else:
            new_user = UserModel(data['name'], data['password'])
            new_user.save_to_db()
            return {"message": "user added successfully"}
