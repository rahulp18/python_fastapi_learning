import uuid

from sqlalchemy import (
    String,
    ForeignKey,
    UniqueConstraint
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from app.db.base import Base

class RolePermission(Base):
    __tablename__="role_permissions"

    __table_args__=(
        UniqueConstraint(
            "role_id",
            "permission_id",
            name="uq_role_permission"
        ),
    )
    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )
    role_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("roles.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    permission_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("permissions.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    role: Mapped["Role"] = relationship(
        back_populates="permissions"
    )

    permission: Mapped["Permission"] = relationship()
