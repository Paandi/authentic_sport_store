from Model.User import UserModel


def authenticate(user, password):
    current_user = UserModel.find_by_name(user)
    if current_user and current_user.pwd == password:
        return current_user
    else:
        {"message": "authentication failed"}


def identity(payload):
    user_id = payload['identity']
    current_user = UserModel.find_by_id(user_id)
    if current_user:
        return current_user
    else:
        return None


