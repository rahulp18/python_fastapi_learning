import uuid
from datetime import datetime

from sqlalchemy import String,ForeignKey,DateTime,func,Boolean,Text
from sqlalchemy.orm import Mapped,mapped_column,relationship

from app.db.base import Base

class Session(Base):
    __tablename__="sessions"

    id:Mapped[str]=mapped_column(
        String(36),
        primary_key=True,
        default=lambda:str(uuid.uuid4())
    )

    user_id:Mapped[str]=mapped_column(
        String(36),
        ForeignKey("users.id",ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    user:Mapped["User"]=relationship(
        back_populates="sessions"
    )
    refresh_token_hash:Mapped[str]=mapped_column(
        String(255),
        nullable=False
    )
    # DEVICE TRACKING
    user_agent:Mapped[str|None]=mapped_column(
        String,
        nullable=True
    )
    ip_address:Mapped[str|None]=mapped_column(
        String(100),
        nullable=True
    )
    # session life cycle
    created_at:Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    last_used_at:Mapped[datetime|None]=mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
    expires_at:Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        nullable=False
    )
    revoked_at:Mapped[datetime|None]=mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
    is_active:Mapped[str]=mapped_column(
        Boolean,
        default=True,
        nullable=False
    )



