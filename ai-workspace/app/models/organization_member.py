import uuid
from datetime import datetime
from sqlalchemy import String,ForeignKey,DateTime,func,UniqueConstraint
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.models.enums import OrganizationRole
from app.db.base import Base


class OrganizationMember(Base):
    __tablename__="organization_members"

    __table_args__=(
        UniqueConstraint(
            "organization_id",
            "user_id",
            name="uq_organization_member"
        ),
    )

    id:Mapped[str]=mapped_column(
        String(36),
        primary_key=True,
        default=lambda:str(uuid.uuid4())
    )
    organization_id:Mapped[str]=mapped_column(
        String(36),
        ForeignKey("organizations.id",ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    organization:Mapped["Organization"]=relationship(
        back_populates="members"
    )
    user_id:Mapped[str]=mapped_column(
        String(36),
        ForeignKey("users.id",ondelete="CASCADE"),
        nullable=True,
        index=True
    )
    user:Mapped["User"]=relationship(
        back_populates="organization_memberships"
    )
    role:Mapped[OrganizationRole]=mapped_column(
        String(36),
        nullable=False,
        default=OrganizationRole.MEMBER
    )
    joined_at:Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )