from sqlalchemy.orm import Session
from app.models import Organization

def create_organization(db:Session,data:dict):
    organization=Organization(
        title=data["title"]
    )

