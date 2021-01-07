from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CameraDetails(BaseModel):
    """
    Service layer: Camera json schema
    """
    brand: str
    model: str
    resolution: int


class DroneDetails(BaseModel):
    """
    Service layer: Drone json schema
    """
    id: Optional[UUID] = None
    name: str
    brand: str
    serial_number: str
    camera: CameraDetails


