from enum import Enum

from pydantic import BaseModel


class SupportedCameras(str, Enum):
    leica = 'LEICA'
    gopro = 'GOPRO'
    canon = 'CANON'


class Camera (BaseModel):
    model: str
    brand: SupportedCameras
    resolution: int
