from fastapi import APIRouter, HTTPException
from starlette.requests import Request

from Domain.Inventory import register_new_drone, retrieve_drones
from Domain.Types.AuthorisationError import AuthorisationError
from Rest.schema.drone_details import DroneDetails
from Rest.schema.user_id import UserId

router = APIRouter(
    prefix="/drones",
    tags=["drones"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def add_new_drone(request: Request, drone: DroneDetails):
    """
    REST endpoint to save a new drone to the inventory
    :param request: Starlette object, contains details about the incoming request
    :param drone: Details about the drone to save
    :return: UUID of the new drone saved into the database
    """
    try:
        user = UserId(id=request.headers['x-fakeauth-x'])
        return register_new_drone(user, drone)
    except AuthorisationError as e:
        raise HTTPException(status_code=403, detail=e.message)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


@router.get("/")
def get_drones():
    """
    Access the drone available in inventory
    :return: List of information about available drones
    """
    return retrieve_drones()
