from functools import wraps
from fastapi import HTTPException
from DataAccess.UserDataAccess import get_right
from Domain.Types.AuthorisationError import AuthorisationError
from Domain.Types.UserRights import UserRights
from Rest.schema.user_id import UserId


def check_write_access(user_id: UserId):
    right = get_right(user_id)
    if right == UserRights.WRITE:
        return True

    return False


def is_allowed_to_write(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if check_write_access(args[0]):
            func(*args, **kwargs)
        else:
            raise AuthorisationError()
    return wrapper
