from sqlalchemy import select

from app.models import Permission

PERMISSIONS = [
    ("workspace.read", "Read workspace"),
    ("workspace.write", "Edit workspace"),
    ("workspace.delete", "Delete workspace"),
    ("member.invite", "Invite members"),
    ("member.remove", "Remove members"),
]


async def seed_permissions(db):
    for key, description in PERMISSIONS:

        existing = await db.execute(
            select(Permission).where(
                Permission.key == key
            )
        )

        if existing.scalar_one_or_none():
            continue

        db.add(
            Permission(
                key=key,
                description=description
            )
        )

    await db.commit()