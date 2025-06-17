"""Migración inicial limpia

Revision ID: 2ad858012645
Revises: 
Create Date: 2025-06-16 17:51:52.917584
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ad858012645'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # 1. Añadir la nueva columna como nullable temporalmente
    with op.batch_alter_table('visitor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('visitor_type', sa.String(length=50), nullable=True))

    # 2. Rellenar los valores existentes con un valor por defecto
    op.execute("UPDATE visitor SET visitor_type = 'Desconocido' WHERE visitor_type IS NULL")

    # 3. Alterar la columna para que sea NOT NULL
    with op.batch_alter_table('visitor', schema=None) as batch_op:
        batch_op.alter_column('visitor_type', nullable=False)

    # 4. Eliminar la antigua columna si existe
    with op.batch_alter_table('visitor', schema=None) as batch_op:
        batch_op.drop_column('Visitor_type')


def downgrade():
    # Revertimos los cambios
    with op.batch_alter_table('visitor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Visitor_type', sa.String(length=50), nullable=True))

    op.execute("UPDATE visitor SET Visitor_type = visitor_type")

    with op.batch_alter_table('visitor', schema=None) as batch_op:
        batch_op.drop_column('visitor_type')
