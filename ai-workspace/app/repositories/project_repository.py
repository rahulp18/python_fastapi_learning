from sqlalchemy.orm import Session
from app.models.project import Project
def create_project(db:Session,input_data:dict):
    project=Project(
        title=input_data["title"],
        description=input_data.get("description"),
        owner_id=input_data["owner_id"]
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def get_all_project(db:Session,owner_id:str):
    return db.query(Project).filter(Project.owner_id==owner_id).all()

def get_project_by_id(db:Session,project_id:str,owner_id:str):
    return db.query(Project).filter(Project.id==project_id , Project.owner_id==owner_id).first()

def update_project(db:Session,project_id:str,owner_id:str,data:dict):
    project=db.query(Project).filter(Project.id==project_id,Project.owner_id==owner_id).first()
    if not project:
        return None
    for key,value in data.items():
        setattr(project,key,value)
    db.commit()
    db.refresh(project)
    return project
def delete_project_by_id(db:Session,project_id:str,owner_id:str ):
    project=db.query(Project).filter(Project.id==project_id,Project.owner_id==owner_id).first()
    if not project:
        return None
    db.delete(project)
    db.commit()
    return project
