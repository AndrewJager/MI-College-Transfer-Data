"""empty message

Revision ID: 7778b8389280
Revises: 9a7434a283f9
Create Date: 2019-08-27 21:56:13.886794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7778b8389280'
down_revision = '9a7434a283f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('datasets', sa.Column('transfer_admitted', sa.Integer(), nullable=True))
    op.add_column('datasets', sa.Column('transfer_applicants', sa.Integer(), nullable=True))
    op.add_column('datasets', sa.Column('transfer_enrolled', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('datasets', 'transfer_enrolled')
    op.drop_column('datasets', 'transfer_applicants')
    op.drop_column('datasets', 'transfer_admitted')
    # ### end Alembic commands ###
