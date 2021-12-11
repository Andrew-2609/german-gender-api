from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import model
import router.noun


def get_all(gender: model.Gender, db: Session):
    query = db.query(model.Noun)

    if hasattr(gender, "name"):
        query = query.filter(model.Noun.gender == gender.name)
    else:
        query = query.filter(model.Noun.gender != "tbd")

    nouns = query.order_by(model.Noun.noun).all()
    return nouns


def get_by_noun(noun: str, db: Session):
    found_noun = db.query(model.Noun).filter(model.Noun.noun == noun).first()

    if not found_noun:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "message": f"Noun '{noun}' was not found",
            "procedure": "If you are sure that it sould exist, please contact me at andrew.agoravai@gmail.com",
            "url": router.noun.router.url_path_for("get_noun", **{"searched_noun": noun})
        })

    return found_noun
