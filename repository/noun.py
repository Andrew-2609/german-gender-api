from sqlalchemy.orm import Session

import model


def get_all(limit: int, db: Session):
    nouns = db.query(model.Noun).limit(limit).all()
    return nouns
