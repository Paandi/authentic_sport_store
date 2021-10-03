from Model.User import UserModel


def authenticate(user, password):
    current_user = UserModel.find_by_name(user)
    if current_user and current_user[2] == password:
        return UserModel(current_user[0], current_user[1], current_user[2])


def identity(payload):
    user_id = payload['identity']
    current_user = UserModel.find_by_id(user_id)
    if current_user:
        return UserModel(current_user[0], current_user[1], current_user[2])
    else:
        return None


