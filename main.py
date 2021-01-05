from fastapi import APIRouter

from Rest.DronesAPI import drones_api

app = APIRouter()


app.include_router(drones_api.router)
