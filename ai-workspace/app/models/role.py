from datetime import datetime
import uuid
from sqlalchemy import String,ForeignKey,DateTime,func,Boolean,UniqueConstraint

from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.db.base import Base

class Role(Base):
    __tablename__="roles"

    __table_args__=(
        UniqueConstraint(
            "workspace_id",
            "name",
            name="uq_workspace_role_name"
        ),
    )

    id:Mapped[str]=mapped_column(
        String(36),
        primary_key=True,
        default=lambda:str(uuid.uuid4())
    )

    workspace_id:Mapped[str]=mapped_column(
        String(36),
        ForeignKey("workspaces.id",ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    name:Mapped[str]=mapped_column(
        String(100),
        nullable=False
    )
    description:Mapped[str]=mapped_column(
        String(255),
        nullable=True
    )
    is_system:Mapped[bool]=mapped_column(
        Boolean,
        default=False,
        nullable=False
    )
    created_at:Mapped[datetime]=mapped_column(
       DateTime(timezone=True),
       server_default=func.now(),
       nullable=False
    )
    updated_at:Mapped[datetime]=mapped_column(
       DateTime(timezone=True),
       server_default=func.now(),
       onupdate=func.now(),
       nullable=False
    )
    workspace:Mapped["Workspace"]=relationship(
        back_populates="roles"
    )
    members: Mapped[list["WorkspaceMember"]] = relationship(
        back_populates="role"
    )
    permissions: Mapped[list["RolePermission"]] = relationship(
        back_populates="role",
        cascade="all, delete-orphan"
    )
