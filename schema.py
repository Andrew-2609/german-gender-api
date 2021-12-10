from pydantic import BaseModel


class Noun(BaseModel):
    id = int
    noun = str
    gender = str

    class Config:
        orm_mode = True
