"""add project status and timestamps

Revision ID: 0fad10b101f5
Revises: 5681e123707a
Create Date: 2026-05-23 12:04:50.715169

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0fad10b101f5'
down_revision: Union[str, Sequence[str], None] = '5681e123707a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""

    # 1. CREATE ENUM TYPE FIRST
    project_status_enum = sa.Enum(
        'CREATED',
        'PLANNING',
        'IN_PROGRESS',
        'COMPLETED',
        name='projectstatus'
    )
    project_status_enum.create(op.get_bind(), checkfirst=True)

    # 2. ADD PROJECTS COLUMNS
    op.add_column(
        'projects',
        sa.Column(
            'status',
            sa.Enum(
                'CREATED',
                'PLANNING',
                'IN_PROGRESS',
                'COMPLETED',
                name='projectstatus'
            ),
            nullable=False,
            server_default='CREATED'
        )
    )

    op.add_column(
        'projects',
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=False
        )
    )

    op.add_column(
        'projects',
        sa.Column(
            'updated_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=False
        )
    )

    # 3. USERS TABLE
    op.add_column(
        'users',
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=False
        )
    )

    op.add_column(
        'users',
        sa.Column(
            'updated_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=False
        )
    )

def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')

    op.drop_column('projects', 'updated_at')
    op.drop_column('projects', 'created_at')
    op.drop_column('projects', 'status')

    # DROP ENUM TYPE LAST
    project_status_enum = sa.Enum(
        name='projectstatus'
    )
    project_status_enum.drop(op.get_bind(), checkfirst=True)
