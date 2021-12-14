"""new database

Revision ID: 72dfda147cfa
Revises: 
Create Date: 2021-12-14 14:20:28.686841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72dfda147cfa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_username', sa.String(length=80), nullable=False),
    sa.Column('activity', sa.String(length=100), nullable=True),
    sa.Column('rating', sa.String(length=25), nullable=True),
    sa.Column('time_elapsed', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.ForeignKeyConstraint(['user_username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('health',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weight_in_pounds', sa.Integer(), nullable=False),
    sa.Column('user_username', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['user_username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('health')
    op.drop_table('activity')
    op.drop_table('user')
    # ### end Alembic commands ###
