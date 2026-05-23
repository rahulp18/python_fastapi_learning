from sqlalchemy.orm import Session
from app.repositories.project_repository import create_project,get_all_project,get_project_by_id,update_project,delete_project_by_id
from app.schemas.project import ProjectInput,ProjectUpdate
def add_project(db:Session,data:ProjectInput,user_id:str):
    payload=data.model_dump()
    payload["owner_id"]=user_id
    return create_project(db,payload)
def get_projects(db:Session,user_id:str):
    return get_all_project(db,user_id)
def get_project(db:Session,project_id:str,user_id:str):
    return get_project_by_id(db,project_id,user_id)
def edit_project(db:Session,project_id:str,owner_id:str,data:ProjectUpdate):
    payload=data.model_dump(exclude_unset=True)
    return update_project(
       db,project_id,
       owner_id,
       payload
    )
def delete_project(db:Session,project_id:str,owner_id:str):
    return delete_project_by_id(db,project_id,owner_id)

    
