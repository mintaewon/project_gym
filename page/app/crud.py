from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.User):
    db_user = models.User(id=user.id,name=user.name ,password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    