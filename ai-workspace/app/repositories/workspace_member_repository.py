from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import WorkspaceMember

class WorkspaceMemberRepository:

    @staticmethod
    async def create(
        db:AsyncSession,
        workspace_id:str,
        user_id:str,
        org_member_id:str,
        role_id:str|None=None
    ):
        member=WorkspaceMember(
            workspace_id=workspace_id,
            user_id=user_id,
            organization_member_id=org_member_id,
            role_id=role_id
        )
        db.add(member)
        await db.flush()
        await db.refresh(member)
        return member
    
    @staticmethod
    async def get_by_user_and_workspace(
        db:AsyncSession,
        workspace_id:str,
        user_id:str
    ):
        result=await db.execute(
            select(WorkspaceMember).where(
                WorkspaceMember.workspace_id==workspace_id,
                WorkspaceMember.user_id==user_id
            )
        )
        return result.scalar_one_or_none()