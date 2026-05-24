import uuid
 
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy import (
    String,
    UniqueConstraint
)

from app.db.base import Base

class Permission(Base):
    __tablename__="permissions"

    __table_args__=(
        UniqueConstraint(
            "key",
            name="uq_permission_key"
        ),
    )
    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )
    key: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True
    )
    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )