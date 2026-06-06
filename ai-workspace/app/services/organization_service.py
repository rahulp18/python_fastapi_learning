from sqlalchemy.ext.asyncio import AsyncSession
from app.core.slug import generate_slug
from app.schemas.user_schema import UserResponseSchema
from app.models.organization_member import OrganizationRole
from app.services.workspace_service import WorkspaceService
from app.repositories.organization_repository import OrganizationRepository
class OrganizationService:

    @staticmethod
    async def create_org_with_workspace(db:AsyncSession,user:UserResponseSchema,org_name:str):
        slug=generate_slug(org_name)
        # create organization
        org=await OrganizationRepository.create(
            db,
            name=org_name,
            slug=slug,
            owner_id=user.id
        )

        # create org membership (OWNER)

        orgMember=await OrganizationRepository.create_membership(
            db,
            organization_id=org.id,
            user_id=user.id,
            role=OrganizationRole.OWNER
        )
        # workspace create
        await WorkspaceService.create_workspace_flow(
            db=db,
            organization=org,
            user=user,
            org_member_id=orgMember.id
        )
        return org
 