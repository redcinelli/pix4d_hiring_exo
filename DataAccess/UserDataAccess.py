from Domain.Types.User import User
from Domain.Types.UserRights import UserRights
from Rest.schema.user_id import UserId

db = [
    {
        'id': 0,
        'username': 'Paul',
        'password': '7acd98403f7b3b573be3fc0124418073a0e2f6d6',
        'right': 1
    },
    {
        'id': 1,
        'username': 'Luap',
        'password': '46e390fdbb26f8191b389a434495678551328cf5',
        'right': 0
    }
]


def get_right(user_id: UserId):
    for user in db:
        if user['id'] == user_id.id:
            return int(user['right'])


def get_user(user_id: UserId):
    for user in db:
        if user['id'] == user_id.id:
            return User(**user)
