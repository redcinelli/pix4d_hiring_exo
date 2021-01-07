from pydantic import BaseModel


class UserId(BaseModel):
    """
    Service layer: user schema
    """
    id: int
