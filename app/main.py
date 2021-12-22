from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

import model
from database import engine
from router import noun, home

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

model.Base.metadata.create_all(engine)

app.include_router(router=noun.router)
app.include_router(router=home.router)
