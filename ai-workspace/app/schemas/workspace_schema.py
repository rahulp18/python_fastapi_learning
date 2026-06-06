from pydantic import Field,BaseModel
class WorkspaceInput(BaseModel):
    name:str=Field(
        min_length=1,
    )
    slug:str=Field(
        min_length=1
    )
    organization_id:str=Field(
        min_length=1
    )
    owner_id:str=Field(
        min_length=1
    )