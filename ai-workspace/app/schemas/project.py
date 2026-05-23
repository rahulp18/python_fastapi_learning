from pydantic import BaseModel
from datetime import datetime
from app.models.enums import ProjectStatus
class ProjectInput(BaseModel):
    title:str
    description:str|None=None

class ProjectResponse(BaseModel):
    id:str
    title:str
    description:str|None
    status:str
    created_at:datetime
    updated_at:datetime

class ProjectUpdate(BaseModel):
    title:str|None=None
    description:str|None=None
    status:ProjectStatus|None=None
