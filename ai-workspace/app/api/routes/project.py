from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.schemas.project import ProjectInput,ProjectResponse,ProjectUpdate
from app.services.project_service import add_project,get_projects,get_project,edit_project,delete_project
from app.api.dependencies.db import get_db
from app.api.dependencies.auth import get_current_user
router=APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.post("/",response_model=ProjectResponse)
async def create(project:ProjectInput,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return add_project(db,project,current_user.id)

@router.get("/",response_model=list[ProjectResponse])
async def all_projects(db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return get_projects(db,current_user.id)
@router.get("/{project_id}",response_model=ProjectResponse)
async def single_project(project_id:str,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return get_project(db,project_id,current_user.id)
@router.patch('/{project_id}',response_model=ProjectResponse)
async def update(project_id:str,data:ProjectUpdate,current_user=Depends(get_current_user),db:Session=Depends(get_db)):
    return edit_project(db,project_id,current_user.id,data)
@router.delete("/{project_id}",response_model=ProjectResponse)
async def delete(project_id:str,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return delete_project(db,project_id,current_user.id)