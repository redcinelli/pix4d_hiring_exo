from pydantic import BaseModel


class UserId(BaseModel):
    id: int
