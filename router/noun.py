from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import database
import model
import schema

from repository import noun

router = APIRouter(
    prefix="/api/nouns",
    tags=["Nouns"]
)


@router.get("/", response_model=List[schema.BaseNoun])
def get_all_nouns(limit: int = 10, db: Session = Depends(database.get_db)):
    return noun.get_all(limit, db)


@router.get("/{noun}", response_model=schema.BaseNoun)
def get_noun(searched_noun: str, db: Session = Depends(database.get_db)):
    found_noun = db.query(model.Noun).filter(model.Noun.noun == searched_noun).first()

    if not found_noun:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Noun {searched_noun} was not found")

    return found_noun
