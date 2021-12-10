from typing import List, Optional

from fastapi import APIRouter, Depends
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
def get_all_nouns(gender: Optional[model.Gender] = None, limit: int = 10,
                  db: Session = Depends(database.get_db)):
    nouns = noun.get_all(gender, limit, db)
    set_appropriate_articles(nouns)
    return nouns


@router.get("/{searched_noun}", response_model=schema.BaseNoun)
def get_noun(searched_noun: str, db: Session = Depends(database.get_db)):
    found_noun = noun.get_by_noun(searched_noun, db)
    set_appropriate_articles(found_noun)
    return found_noun


def set_appropriate_articles(noun_s):
    if type(noun_s) == model.Noun:
        check_noun_gender(noun_s)
    elif type(noun_s) == list:
        for entry in noun_s:
            check_noun_gender(entry)


def check_noun_gender(analysed_noun: model.Noun):
    if analysed_noun.gender == model.Gender.masculine:
        analysed_noun.articles = ({
            "nominative": "der",
            "accusative": "den",
            "dative": "dem",
            "genitive": "des"
        })
    elif analysed_noun.gender == model.Gender.feminine:
        analysed_noun.articles = ({
            "nominative": "die",
            "accusative": "die",
            "dative": "den",
            "genitive": "der"
        })
    elif analysed_noun.gender == model.Gender.neutral:
        analysed_noun.articles = ({
            "nominative": "das",
            "accusative": "das",
            "dative": "dem",
            "genitive": "des"
        })
