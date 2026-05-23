from sqlalchemy import String,DateTime,func
from sqlalchemy.orm import Mapped,mapped_column,relationship
import uuid
from app.db.base import Base
from datetime import datetime
class User(Base):
    __tablename__="users"

    id:Mapped[str]=mapped_column(
        String,
        primary_key=True,
        default=lambda:str(uuid.uuid4()),
    )
    name:Mapped[str]=mapped_column(
        String(100)
    )
    email:Mapped[str]=mapped_column(
        String(255),
        unique=True,
        index=True
    )
    password:Mapped[str]=mapped_column(
        String
    )
    projects:Mapped[list['Project']]=relationship(
        back_populates="owner",
        cascade="all, delete-orphan"
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