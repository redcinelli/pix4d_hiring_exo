from enum import Enum
from uuid import UUID

from pydantic import BaseModel
from datetime import datetime

from Domain.Types.Camera import Camera
from Domain.Types.User import User


class SupportedDrones(str, Enum):
    sensefly = 'SENSEFLY'
    dji = 'DJI'
    parrot = 'PARROT'


class Drone(BaseModel):
    id: UUID
    name: str
    serial_number: str
    brand: SupportedDrones
    camera: Camera
    check_in: datetime
    user: User
