import uuid
from datetime import datetime

from sqlalchemy import String,ForeignKey,DateTime,UniqueConstraint,func
from sqlalchemy.orm import Mapped,mapped_column,relationship

from app.db.base import Base

class WorkspaceMember(Base):
    __tablename__="workspace_members"
    __table_args__=(
        UniqueConstraint(
         "workspace_id",
         "user_id",
         name="uq_workspace_member"
        ),
    )
    
    id:Mapped[str]=mapped_column(
        String(36),
        primary_key=True,
        default=lambda:str(uuid.uuid4())
    )
    workspace_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    organization_member_id:Mapped[str]=mapped_column(
        String(36),
        ForeignKey("organization_members.id",ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    user_id:Mapped[str]=mapped_column(
        String(36),
        ForeignKey("users.id",ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    role_id: Mapped[str | None] = mapped_column(
        String(36),
        ForeignKey("roles.id", ondelete="SET NULL"),
        nullable=True,
        index=True
    )

    joined_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    workspace: Mapped["Workspace"] = relationship(
        back_populates="members"
    )

    organization_member: Mapped["OrganizationMember"] = relationship()

    user: Mapped["User"] = relationship(
        back_populates="workspace_memberships"
    )

    role: Mapped["Role"] = relationship(
        back_populates="members"
    )
