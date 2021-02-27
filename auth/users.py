import random
from utils.storage import Json

USERS = Json('data/users.json')


def generate_id(l=64):
    id = random.randint(
        int('1'+'0'*(random.randint(20, l-1))),
        int('9'*l)
    )
    return str(id) if str(id) not in USERS else generate_id(l)


class User:
    def __init__(self, id):
        self.id = id
    
    @staticmethod
    def create_user(name, user):
        id = generate_id()
        model = User.structure()
        model['id'] = id
        model['name'] = name
        model['user'] = user
        USERS[id] = model
    
    def structure():
        return {
            'user': None,
            'name': None,
            'id': None,
            'avatar': None
        }
