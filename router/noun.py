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
    nouns = noun.get_all(limit, db)
    set_appropriate_articles(nouns)
    return nouns


@router.get("/{noun}", response_model=schema.BaseNoun)
def get_noun(searched_noun: str, db: Session = Depends(database.get_db)):
    found_noun = db.query(model.Noun).filter(model.Noun.noun == searched_noun).first()

    if not found_noun:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Noun {searched_noun} was not found")

    return found_noun


def set_appropriate_articles(nouns: List[model.Noun]):
    for entry in nouns:
        if entry.gender == model.Gender.masculine:
            entry.articles = ({
                "nominative": "der",
                "accusative": "den",
                "dative": "dem",
                "genitive": "des"
            })
        elif entry.gender == model.Gender.feminine:
            entry.articles = ({
                "nominative": "die",
                "accusative": "die",
                "dative": "den",
                "genitive": "der"
            })
        elif entry.gender == model.Gender.neutral:
            entry.articles = ({
                "nominative": "das",
                "accusative": "das",
                "dative": "dem",
                "genitive": "des"
            })
