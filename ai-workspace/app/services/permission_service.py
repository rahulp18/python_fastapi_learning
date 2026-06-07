from fastapi import HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.organization_member import OrganizationRole,OrganizationMember
from app.models import WorkspaceMember
from sqlalchemy import select


class PermissionService:
    @staticmethod
    async def check_workspace_permission(
        db:AsyncSession,
        user_id:str,
        workspace_id:str,
        permission_key:str
    ):
        result=await db.execute(
            select(WorkspaceMember).where(
                WorkspaceMember.user_id==user_id,
                WorkspaceMember.workspace_id==workspace_id
            )
        )
        member=result.scalar_one_or_none()

        if not member:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not a workspace member"
            )
        role_permission=[
            rp.permission.key for rp in member.role.permissions
        ]

        if permission_key not in role_permission:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied"
            )
        return True
    
    @staticmethod
    async def check_organization_role(db:AsyncSession,user_id:str,org_id:str,role:OrganizationRole):
        result=await db.execute(
            select(OrganizationMember).where(
                OrganizationMember.user_id==user_id,
                OrganizationMember.organization_id==org_id,
                OrganizationMember.role==role
            )
        )
        member=result.scalar_one_or_none()

        if not member:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied"
            )
        return True