from fastapi import FastAPI

import model
from database import engine
from router import noun

app = FastAPI()

model.Base.metadata.create_all(engine)

app.include_router(router=noun.router)
