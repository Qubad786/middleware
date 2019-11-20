"""Two-Factor auth

Revision ID: f2e8d8e7fd57
Revises: 514ce6934952
Create Date: 2019-11-19 21:01:50.682690+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2e8d8e7fd57'
down_revision = '514ce6934952'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('system_twofactorauthentication',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('otp_digits', sa.Integer(), nullable=False),
    sa.Column('secret', sa.String(length=16), nullable=True),
    sa.Column('window', sa.Integer(), nullable=False),
    sa.Column('interval', sa.Integer(), nullable=False),
    sa.Column('services', sa.TEXT(), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_system_twofactorauthentication'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('system_twofactorauthentication')
    # ### end Alembic commands ###
