from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import model


def get_all(gender: model.Gender, limit: int, db: Session):
    query = db.query(model.Noun)

    if hasattr(gender, "name"):
        query = query.filter(model.Noun.gender == gender.name)

    nouns = query.limit(limit).all()
    return nouns


def get_by_noun(noun: str, db: Session):
    found_noun = db.query(model.Noun).filter(model.Noun.noun == noun).first()

    if not found_noun:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Noun '{noun}' was not found")

    return found_noun
