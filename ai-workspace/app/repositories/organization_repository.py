from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Organization,OrganizationMember,Workspace,WorkspaceMember
from sqlalchemy import select
from app.models.enums import OrganizationRole


class OrganizationRepository:

    @staticmethod
    async def create(db:AsyncSession,name:str,slug:str,owner_id:str)->Organization:

        organization=Organization(
            name=name,
            slug=slug,
            owner_id=owner_id
        )
        db.add(organization)

        await db.flush()
        await db.refresh(organization)
        return organization
    @staticmethod
    async def get_by_slug(db:AsyncSession,slug:str)->Organization:
        statement=select(Organization).where(
            Organization.slug==slug
        )
        result=await db.execute(statement)
        
        return result.scalar_one_or_none()
        
    @staticmethod
    async def create_membership(
        db:AsyncSession,
        organization_id:str,
        user_id:str,
        role:OrganizationRole
    )->OrganizationMember:
        membership=OrganizationMember(
            organization_id=organization_id,
            user_id=user_id,
            role=role
        )
        db.add(membership)
        await db.flush()
        await db.refresh(membership)
        return membership
 
 