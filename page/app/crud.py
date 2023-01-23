from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.User):
    fake_hashed_password = user.password + "notreallyhashed"
    print(fake_hashed_password)
    db_user = models.User(id=user.id,name=user.name ,password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user