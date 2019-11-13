"""Add "updated_at" column to Rule

Revision ID: c17f01adbe31
Revises: b50c705fea80
Create Date: 2016-05-27 15:51:58.168840

"""

# revision identifiers, used by Alembic.
revision = 'c17f01adbe31'
down_revision = 'b50c705fea80'

from alembic import op
import sqlalchemy as sa
import polylogyx.database


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rule',
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=sa.func.now()))
    ### end Alembic commands ###

    op.create_index('idx__rule__updated_at', 'rule', ['updated_at'])


def downgrade():
    op.drop_index('idx__rule__updated_at')
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rule', 'updated_at')
    ### end Alembic commands ###