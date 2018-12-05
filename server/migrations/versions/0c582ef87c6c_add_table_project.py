"""Add table Project

Revision ID: 0c582ef87c6c
Revises: b04c8ccef6d1
Create Date: 2018-12-05 12:02:02.502078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c582ef87c6c'
down_revision = 'b04c8ccef6d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idUser', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('describe', sa.String(length=1000), nullable=True),
    sa.Column('startDate', sa.DateTime(), nullable=True),
    sa.Column('endDate', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['idUser'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_project_startDate'), 'project', ['startDate'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_project_startDate'), table_name='project')
    op.drop_table('project')
    # ### end Alembic commands ###
