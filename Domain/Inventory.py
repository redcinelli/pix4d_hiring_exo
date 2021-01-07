import uuid
from datetime import datetime

from DataAccess.InventoryDataAcess import persist_inventory_item, read_drone_info
from DataAccess.UserDataAccess import get_user
from Domain.Authentication import is_allowed_to_write
from Domain.Types.Camera import Camera, SupportedCameras
from Domain.Types.Drone import Drone, SupportedDrones
from Domain.Types.User import User
from Rest.schema.drone_details import DroneDetails
from Rest.schema.user_id import UserId

drones = []


@is_allowed_to_write
def register_new_drone(user_id: UserId, drone_info: DroneDetails):
    """
    Domain layer: Save new drone to the database if information checks out
    :param user_id: User info
    :param drone_info: drone details
    :return: drone id
    """
    drone_id = uuid.uuid4()

    drone = Drone(
        id=drone_id,
        name=drone_info.name,
        serial_number=drone_info.serial_number,
        brand=SupportedDrones(drone_info.brand),
        camera=Camera(
            model=drone_info.camera.model,
            brand=SupportedCameras(drone_info.camera.brand),
            resolution=drone_info.camera.resolution),
        check_in=datetime.utcnow(),
        user=User(**get_user(user_id).dict())
    )

    persist_inventory_item(drone)

    return drone.id


def retrieve_drones():
    """
    Domain layer: Get drones available in the inventory
    :return: list of available drones
    """
    return read_drone_info()

