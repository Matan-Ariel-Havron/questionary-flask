"""empty message

Revision ID: 52c343cf1448
Revises: a956cb15eba0
Create Date: 2020-07-13 15:16:11.968707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52c343cf1448'
down_revision = 'a956cb15eba0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('relationship_object', sa.Column('confirmed', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('relationship_object', 'confirmed')
    # ### end Alembic commands ###
