
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Role,RolePermission
from app.repositories.permission_repository import PermissionRepository
class RoleService:
    @staticmethod
    async def seed_default_roles(db:AsyncSession,workspace_id:str):
        admin=Role(
           workspace_id=workspace_id,
           name="ADMIN",
           is_system=True
        )
        member=Role(
            workspace_id=workspace_id,
            name="MEMBER",
            is_system=True
        )
        guest=Role(
            workspace_id=workspace_id,
            name="GUEST",
            is_system=True
        )
        db.add_all([admin,member,guest])
        await db.flush()

        permissions=await PermissionRepository.get_all(db)

        perm_map={p.key:p for p in permissions}

        def attach(role,keys):
            for k in keys:
                if k in perm_map:
                    db.add(RolePermission(
                        role_id=role.id,
                        permission_id=perm_map[k].id
                    ))
        attach(admin,["workspace.read","workspace.write","member.invite","member.remove"])
        attach(member,["workspace.read"])
        attach(guest,["workspace.read"])

        return {
            "admin":admin,
            "member":member,
            "guest":guest
        }

        