
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.workspace_repository import WorkspaceRepository
from app.schemas.user_schema import UserResponseSchema
from app.services.role_service import RoleService
from app.repositories.workspace_member_repository import WorkspaceMemberRepository
class WorkspaceService:
    @staticmethod
    async def create_workspace_flow(db:AsyncSession,organization,user:UserResponseSchema,org_member_id:str):

        # create workspace
        workspace=await WorkspaceRepository.create(
            db,
            name=f"{user.username}-workspace",
            organization_id=organization.id,
            slug=f"{user.username}-ws"
        )
        # send roles
        roles=await RoleService.seed_default_roles(db,workspace.id)
        admin_role=roles["admin"]
        await WorkspaceMemberRepository.create(
            db,
            workspace_id=workspace.id,
            user_id=user.id,
            org_member_id=org_member_id,
            role_id=admin_role.id
        )
        return workspace
        
