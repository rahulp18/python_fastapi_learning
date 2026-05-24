from sqlalchemy import String,ForeignKey,DateTime,func
from app.db.base import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
 
from datetime import datetime
import uuid
class Organization(Base):
    __tablename__="organizations"
    
    id:Mapped[str]=mapped_column(
        String(36),
        default=lambda:str(uuid.uuid4()),
        primary_key=True
    )
    slug:Mapped[str]=mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )
    name:Mapped[str]=mapped_column(
        String(255),
        nullable=False

    )
    logo:Mapped[str|None]=mapped_column(
        String(500),
        nullable=True,
    )
    brand_color:Mapped[str|None]=mapped_column(
        String(20),
        nullable=True
    )
    owner_id:Mapped[str]=mapped_column(
        String(36),
        ForeignKey("users.id",ondelete="CASCADE"),
        nullable=False,
        index=True

    )
    owner:Mapped["User"]=relationship(
         back_populates="organizations"
    )
    workspaces:Mapped[list["Workspace"]]=relationship(
        back_populates="organization",
        cascade="all,delete-orphan"
    )
    members: Mapped[list["OrganizationMember"]] = relationship(
    back_populates="organization",
    cascade="all, delete-orphan"
    )
    created_at:Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    updated_at:Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )
