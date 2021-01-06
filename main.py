from fastapi import FastAPI

from Rest.DronesAPI import drones_api

app = FastAPI()

app.include_router(drones_api.router)
