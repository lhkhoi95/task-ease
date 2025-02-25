from sqlalchemy.orm import Session
from app.db.models import User
from app.schemas.user import UserCreate


def create_user(db: Session, user: UserCreate):
    # Hash password in real-world apps
    db_user = User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(User).all()
