from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from Rest.DronesAPI import drones_api

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(drones_api.router)
