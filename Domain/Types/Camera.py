from enum import Enum

from pydantic import BaseModel


class SupportedCameras(str, Enum):
    """
    Domain layer: Official list of camera brand supported by the company
    """
    leica = 'LEICA'
    gopro = 'GOPRO'
    canon = 'CANON'


class Camera (BaseModel):
    """
    Domain layer: Camera details
    """
    model: str
    brand: SupportedCameras
    resolution: int
