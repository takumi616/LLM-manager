"""Alter_table_name_to_large_language_models

Revision ID: 803e9d212f6f
Revises: 827782979504
Create Date: 2025-07-12 09:41:52.382113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '803e9d212f6f'
down_revision: Union[str, Sequence[str], None] = '827782979504'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('large_language_models',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('model', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('free', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_large_language_models_name'), 'large_language_models', ['name'], unique=False)
    op.drop_index(op.f('ix_largelanguagemodel_name'), table_name='largelanguagemodel')
    op.drop_table('largelanguagemodel')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('largelanguagemodel',
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('model', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('free', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('largelanguagemodel_pkey'))
    )
    op.create_index(op.f('ix_largelanguagemodel_name'), 'largelanguagemodel', ['name'], unique=False)
    op.drop_index(op.f('ix_large_language_models_name'), table_name='large_language_models')
    op.drop_table('large_language_models')
    # ### end Alembic commands ###
