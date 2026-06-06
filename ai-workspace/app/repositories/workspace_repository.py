
from sqlalchemy.ext.asyncio import AsyncSession
 
from app.models.workspace import Workspace
class WorkspaceRepository:
 
    @staticmethod
    async def create(db:AsyncSession,name:str,organization_id:str,slug:str):
         workspace=Workspace(
            name=name,
            organization_id=organization_id,
            slug=slug      
         )
         db.add(workspace)
         await db.flush()
         await db.refresh(workspace)
         return workspace
