"""add models

Revision ID: 71bc198c11bd
Revises:
Create Date: 2023-10-02 16:11:49.878362

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '71bc198c11bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('url',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('target_url', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('clicks_count', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_url'))
    )
    op.create_index(op.f('ix_url_key'), 'url', ['key'], unique=True)
    op.create_index(op.f('ix_url_target_url'), 'url', ['target_url'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_url_target_url'), table_name='url')
    op.drop_index(op.f('ix_url_key'), table_name='url')
    op.drop_table('url')
    # ### end Alembic commands ###