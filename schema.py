import enum

from pydantic import BaseModel


class BaseNoun(BaseModel):
    noun: str
    gender: enum.Enum
    articles: dict

    class Config:
        orm_mode = True
