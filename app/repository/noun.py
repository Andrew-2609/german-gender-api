from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

import model
import router.noun
import schema


def get_all(gender: Optional[model.Gender], page: int, size: int, db: Session):
    if gender:
        query = text(
            "SELECT noun, gender FROM nouns WHERE gender= :gender "
            "AND id>=(SELECT id FROM nouns LIMIT :page,1) LIMIT :size",
        )
        result = db.execute(query, {"gender": gender.name, "page": page * size, "size": size}).all()
    else:
        query = text(
            "SELECT noun, gender FROM nouns WHERE gender != :gender "
            "AND id>=(SELECT id FROM nouns LIMIT :page,1) LIMIT :size",
        )
        result = db.execute(query, {"gender": "tbd", "page": page * size, "size": size}).all()

    return [schema.BaseNoun(noun=r[0], gender=r[1]) for r in result]


def get_by_noun(noun: str, db: Session):
    found_noun = db.query(model.Noun).filter(model.Noun.noun == noun).first()

    if not found_noun:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "message": f"Noun '{noun}' was not found",
            "procedure": "If you are sure that it sould exist, please contact me at andrew.agoravai@gmail.com",
            "url": router.noun.router.url_path_for("get_noun", **{"searched_noun": noun})
        })

    return found_noun
