import enum
from sqlalchemy import Column
from sqlalchemy.types import String, Integer, Enum

from database import Base


class Gender(enum.Enum):
    masculine = "masculine"
    feminine = "feminine"
    neutral = "neutral"


class Noun(Base):
    __tablename__ = "nouns"

    id = Column(Integer, primary_key=True, index=True)
    noun = Column(String(36), unique=True, nullable=False)
    gender = Column(Enum(Gender), nullable=False)
