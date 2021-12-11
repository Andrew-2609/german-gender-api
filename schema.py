import enum
from typing import Optional

from pydantic import BaseModel


class BaseNoun(BaseModel):
    noun: str
    gender: enum.Enum

    class Config:
        orm_mode = True


class NounWithArticles(BaseNoun):
    articles: Optional[dict]
