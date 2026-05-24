from app.db.base import Base
from sqlalchemy import String,ForeignKey,DateTime,func,UniqueConstraint
from sqlalchemy.orm import Mapped,mapped_column,relationship
import uuid
from datetime import datetime

class Workspace(Base):
    __tablename__="workspaces"
   
    __table_args__=(
        UniqueConstraint(
            "organization_id",
            "slug",
            name="uq_workspace_slug_per_org"
        ),
    )
    id:Mapped[str]=mapped_column(
        String(36),
        default=lambda:str(uuid.uuid4()),
        primary_key=True
    )
    name:Mapped[str]=mapped_column(
        String(255),
        nullable=False,
    )
    organization_id:Mapped[str]=mapped_column(
        String(36),
        ForeignKey("organizations.id",ondelete="CASCADE"),
        nullable=False,
        index=True,    
    )
    organization:Mapped["Organization"]=relationship(
        back_populates="workspaces"
    )
    slug:Mapped[str]=mapped_column(
        String(255),
        index=True,
        nullable=False
    )
    created_at:Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at:Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )
    members: Mapped[list["WorkspaceMember"]] = relationship(
        back_populates="workspace",
        cascade="all, delete-orphan"
    )
    roles: Mapped[list["Role"]] = relationship(
        back_populates="workspace",
        cascade="all, delete-orphan"
    )
    