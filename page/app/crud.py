from sqlalchemy.orm import Session


from . import models, schemas

def get_user(db: Session, user_email: str):
    return db.query(models.User).filter(models.User.email == user_email).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email,name=user.name ,password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_item(db:Session, data:schemas.Data):
    db_item = models.Item(weather=data.weather, datetime=data.datetime, use=data.use)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item