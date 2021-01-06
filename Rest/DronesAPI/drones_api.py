from typing import Optional

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
    try:
        user = UserId(id=request.headers['x-fakeauth-x'])
        register_new_drone(user, drone)
    except AuthorisationError as e:
        raise HTTPException(status_code=403, detail=e.message)
    return None


@router.get("/")
def get_drones(brand: Optional[str] = None, camera_brand: Optional[str] = None, name: Optional[str] = None, q: Optional[str] = None):
    return retrieve_drones()
