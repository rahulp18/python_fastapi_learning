from sqlalchemy.orm import Session
from app.models.user import User


def create_user(db:Session,user_data:dict):
    user=User(
        name=user_data["name"],
        email=user_data["email"],
        password=user_data["password"]
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db:Session,email:str):
     try:
          return (
               db.query(User).filter(User.email==email).first()
          )
     except:
          return None
          
     