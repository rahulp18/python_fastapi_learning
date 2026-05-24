from datetime import datetime
import uuid

from sqlalchemy import (
    String,
    ForeignKey,
    DateTime,
    func
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.db.base import Base


class Invitation(Base):
    __tablename__ = "invitations"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    organization_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    workspace_id: Mapped[str | None] = mapped_column(
        String(36),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=True,
        index=True
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    invited_by_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    organization_role: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="ORG_MEMBER"
    )

    workspace_role_id: Mapped[str | None] = mapped_column(
        String(36),
        ForeignKey("roles.id", ondelete="SET NULL"),
        nullable=True
    )

    token: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        unique=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="PENDING"
    )

    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    accepted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    organization: Mapped["Organization"] = relationship()

    workspace: Mapped["Workspace"] = relationship()

    invited_by: Mapped["User"] = relationship()

    workspace_role: Mapped["Role"] = relationship()