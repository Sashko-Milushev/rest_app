import json

USERS_FILE_PATH = './db/users.txt'


def register(username, password):
    user_object = {
        'username': username,
        'password': password
    }

    user_json = json.dumps(user_object)
    with open(USERS_FILE_PATH, 'r+') as file:
        for user_line in file:
            existing_user = json.loads(user_line.strip())
            if existing_user['username'] == username:
                return False
        file.write(user_json + '\n')
        return True


def login(username, password):
    with open(USERS_FILE_PATH, 'r') as file:
        for user_line in file:
            existing_user = json.loads(user_line.strip())
            if existing_user['username'] == username and existing_user['password'] == password:
                return True
        return False
