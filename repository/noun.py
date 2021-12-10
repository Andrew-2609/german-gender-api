from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import model


def get_all(limit: int, db: Session):
    nouns = db.query(model.Noun).limit(limit).all()
    return nouns


def get_one(searched_noun: str, db: Session):
    found_noun = db.query(model.Noun).filter(model.Noun.noun == searched_noun).first()

    if not found_noun:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Noun {searched_noun} was not found")

    return found_noun
