from app.db.base import Base
from sqlalchemy import String,ForeignKey,Enum,DateTime,func
from sqlalchemy.orm import Mapped,mapped_column,relationship
import uuid
from app.models.enums import ProjectStatus
from datetime import datetime
class Project(Base):
    __tablename__="projects"
    id:Mapped[str]=mapped_column(
     String,
     primary_key=True,
     default=lambda:str(uuid.uuid4())
    )
    title:Mapped[str]=mapped_column(
        String(400),
    )
    description:Mapped[str|None]=mapped_column(
        String,
        nullable=True    
    )
    owner_id:Mapped[str]=mapped_column(
        ForeignKey("users.id")
    )
    owner:Mapped["User"]=relationship(
        back_populates="projects"
    )
    status:Mapped[ProjectStatus]=mapped_column(
        Enum(ProjectStatus),
        server_default=ProjectStatus.CREATED
    )
    created_at:Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at:Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )


    
