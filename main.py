from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

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


@app.get("/")
def access_static():
    response = RedirectResponse(url="/index.html")
    return response


app.mount("/", StaticFiles(directory="frontend/build"), name="static")



