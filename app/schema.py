from pydantic import BaseModel

import model


class BaseNoun(BaseModel):
    noun: str
    gender: model.Gender

    class Config:
        orm_mode = True
