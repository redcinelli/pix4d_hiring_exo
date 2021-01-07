from Domain.Types.Drone import Drone

db = []


def persist_inventory_item(drone: Drone):
    """
    Data access layer, act a the database for now
    :param drone: drone details to be saved
    :return: None
    """
    db.append(drone)


def read_drone_info():
    """
    Data access layer to read from the database
    :return: list of available drones
    """
    return db