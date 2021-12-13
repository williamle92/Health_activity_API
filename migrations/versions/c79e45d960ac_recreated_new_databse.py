"""recreated new databse

Revision ID: c79e45d960ac
Revises: fa561499360e
Create Date: 2021-12-12 22:05:29.448561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c79e45d960ac'
down_revision = 'fa561499360e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('health_log_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weight_in_pounds', sa.Integer(), nullable=False),
    sa.Column('user_username', sa.String(length=60), nullable=False),
    sa.ForeignKeyConstraint(['user_username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('health_log_model')
    # ### end Alembic commands ###
