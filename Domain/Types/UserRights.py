from enum import IntEnum


class UserRights(IntEnum):
    """
    Domain layer: user rights representation
    """
    READ = 0
    WRITE = 1
