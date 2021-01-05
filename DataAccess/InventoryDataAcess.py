from Domain.Types.Drone import Drone

db = []


def persist_inventory_item(drone: Drone):
    db.append(drone)


def read_drone_info():
    return db