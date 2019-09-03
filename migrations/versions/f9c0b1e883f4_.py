"""empty message

Revision ID: f9c0b1e883f4
Revises: 27e11e689077
Create Date: 2019-09-02 19:19:56.568609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9c0b1e883f4'
down_revision = '27e11e689077'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('colleges', sa.Column('transfer_website', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('colleges', 'transfer_website')
    # ### end Alembic commands ###