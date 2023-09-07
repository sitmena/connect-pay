"""initial

Revision ID: 06d20931fb97
Revises: 
Create Date: 2023-09-06 15:02:27.636969

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06d20931fb97'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('integrator', sa.String(), nullable=True),
    sa.Column('request', sa.JSON(), nullable=True),
    sa.Column('response', sa.JSON(), nullable=True),
    sa.Column('amount', sa.DECIMAL(), nullable=True),
    sa.Column('status', sa.Enum('PENDING', 'SUCCESS', 'FAILED', name='paymentstatus'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_payment_id'), 'payment', ['id'], unique=False)
    op.create_index(op.f('ix_payment_integrator'), 'payment', ['integrator'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('external_id', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('external_id')
    )
    op.create_index(op.f('ix_users_user_name'), 'users', ['user_name'], unique=True)
    op.create_table('integrator_config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('providers', sa.Enum('HyperPay', 'PayPal', name='providers'), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('config_data', sa.JSON(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_integrator_config_id'), 'integrator_config', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_integrator_config_id'), table_name='integrator_config')
    op.drop_table('integrator_config')
    op.drop_index(op.f('ix_users_user_name'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_payment_integrator'), table_name='payment')
    op.drop_index(op.f('ix_payment_id'), table_name='payment')
    op.drop_table('payment')
    # ### end Alembic commands ###