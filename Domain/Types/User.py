from pydantic import BaseModel

from Domain.Types.UserRights import UserRights


class User(BaseModel):
    """
    Domain layer: User representation
    """
    id: int
    username: str
    password: str
    right: UserRights
