from functools import wraps
from DataAccess.UserDataAccess import get_right
from Domain.Types.AuthorisationError import AuthorisationError
from Domain.Types.UserRights import UserRights
from Rest.schema.user_id import UserId


def check_write_access(user_id: UserId):
    """
    Business logic layer: Check the given user has right to write to the database
    :param user_id: information about the user
    :return: boolean
    """
    right = get_right(user_id)
    if right == UserRights.WRITE:
        return True

    return False


def is_allowed_to_write(func):
    """
    Business logic decorator: Perform read access checks
    :param func:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if check_write_access(args[0]):
            func(*args, **kwargs)
        else:
            raise AuthorisationError()
    return wrapper
