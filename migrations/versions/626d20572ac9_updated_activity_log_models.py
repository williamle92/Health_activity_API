"""updated activity log models

Revision ID: 626d20572ac9
Revises: 8e7c71572e65
Create Date: 2021-12-12 23:56:09.194488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '626d20572ac9'
down_revision = '8e7c71572e65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    op.drop_table('activity_log')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activity_log',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('activity', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('rating', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('time_elapsed', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=300), autoincrement=False, nullable=True),
    sa.Column('user_username', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_username'], ['user.username'], name='activity_log_user_username_fkey'),
    sa.PrimaryKeyConstraint('id', name='activity_log_pkey')
    )
    op.drop_table('activity')
    # ### end Alembic commands ###