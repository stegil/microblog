"""empty message

Revision ID: ab2a83137fbb
Revises: d163daa8429d
Create Date: 2022-09-02 20:46:30.559898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab2a83137fbb'
down_revision = 'd163daa8429d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('published_date', sa.Date(), nullable=True),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('publish', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_published_date'), 'post', ['published_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_published_date'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
