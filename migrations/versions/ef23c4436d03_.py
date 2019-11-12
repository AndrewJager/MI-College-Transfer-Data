"""empty message

Revision ID: ef23c4436d03
Revises: f9c0b1e883f4
Create Date: 2019-11-12 10:18:23.217860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef23c4436d03'
down_revision = 'f9c0b1e883f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('datasets', sa.Column('max_credits_2yr', sa.Integer(), nullable=True))
    op.add_column('datasets', sa.Column('max_credits_4yr', sa.Integer(), nullable=True))
    op.add_column('datasets', sa.Column('min_transfer_grade', sa.String(), nullable=True))
    op.add_column('datasets', sa.Column('total_enrollment', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('datasets', 'total_enrollment')
    op.drop_column('datasets', 'min_transfer_grade')
    op.drop_column('datasets', 'max_credits_4yr')
    op.drop_column('datasets', 'max_credits_2yr')
    # ### end Alembic commands ###