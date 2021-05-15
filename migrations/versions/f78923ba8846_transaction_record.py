
from alembic import op
import sqlalchemy as sa



revision = 'f78923ba8846'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('transaction_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('modified_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('delete_time', sa.DateTime(), nullable=True),
    sa.Column('price', sa.DECIMAL(), nullable=False),
    sa.Column('amount', sa.DECIMAL(), nullable=False),
    sa.Column('type', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )



def downgrade():
    op.drop_table('transaction_log')
