from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CameraDetails(BaseModel):
    brand: str
    model: str
    resolution: int


class DroneDetails(BaseModel):
    id: Optional[UUID] = None
    name: str
    brand: str
    serial_number: str
    camera: CameraDetails


