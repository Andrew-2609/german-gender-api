from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import database
import model
import schema

router = APIRouter(
    prefix="/api/noun",
    tags=["Nouns"]
)


@router.get("/", response_model=List[schema.BaseNoun])
def get_all_nouns(limit: int = 10, db: Session = Depends(database.get_db)):
    nouns = db.query(model.Noun).limit(limit).all()
    return nouns
