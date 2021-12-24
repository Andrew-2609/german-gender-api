from typing import Optional

from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session

import database
import docs.noun
import model
import schema
from repository import noun

router = APIRouter(
    prefix="/api/v1/nouns",
    tags=["Nouns"]
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=dict,
            responses=docs.noun.get_all_nouns_responses)
def get_all_nouns(
        gender: Optional[model.Gender] = None,
        page: int = Query(0, ge=0),
        size: int = Query(10, ge=1),
        db: Session = Depends(database.get_db)
):
    nouns = noun.get_all(gender, page, size, db)
    return {"content": nouns, "page": page, "size": size}


@router.get("/{searched_noun}", status_code=status.HTTP_200_OK, response_model=schema.BaseNoun,
            responses=docs.noun.get_noun_responses)
def get_noun(searched_noun: str, db: Session = Depends(database.get_db)):
    found_noun = noun.get_by_noun(searched_noun.capitalize(), db)
    return found_noun
