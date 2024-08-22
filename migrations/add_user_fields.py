from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('user', sa.Column('profession', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('company_name', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('phone_number', sa.String(length=20), nullable=True))

def downgrade():
    op.drop_column('user', 'profession')
    op.drop_column('user', 'company_name')
    op.drop_column('user', 'phone_number')
