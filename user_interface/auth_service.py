import json


def register(username, password):
    user_object = {
        'username': username,
        'password': password
    }

    user_json = json.dumps(user_object)
    with open('./db/users.txt', 'r+') as file:
        for user_line in file:
            existing_user = json.loads(user_line.strip())
            if existing_user['username'] == username:
                return False
        file.write(user_json + '\n')
        return True
