from sqlalchemy import String,DateTime,func
from sqlalchemy.orm import Mapped,mapped_column,relationship
import uuid
from app.db.base import Base
from datetime import datetime
 
class User(Base):
    __tablename__="users"

    id:Mapped[str]=mapped_column(
        String(36),
        primary_key=True,
        default=lambda:str(uuid.uuid4()),
    )
    name:Mapped[str]=mapped_column(
        String(100),
        nullable=False
    )
    username:Mapped[str]=mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )
    email:Mapped[str]=mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )
    password:Mapped[str]=mapped_column(
        String(255),
        nullable=False
    )
    projects:Mapped[list['Project']]=relationship(
        back_populates="owner",
        cascade="all, delete-orphan"
    )
    organizations:Mapped[list["Organization"]]=relationship(
        back_populates="owner",
        cascade="all,delete-orphan"
    )
    organization_memberships:Mapped[list["OrganizationMember"]]=relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )
    workspace_memberships: Mapped[list["WorkspaceMember"]] = relationship(
    back_populates="user",
    cascade="all, delete-orphan"
    )
    sessions:Mapped[list["Session"]]=relationship(
        back_populates="user",
        cascade="all, delete-orphan"
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
  