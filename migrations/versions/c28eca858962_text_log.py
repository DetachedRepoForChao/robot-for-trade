from alembic import op
import sqlalchemy as sa

revision = 'c28eca858962'
down_revision = 'f78923ba8846'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('text_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('modified_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('delete_time', sa.DateTime(), nullable=True),
    sa.Column('contents', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('text_log')

