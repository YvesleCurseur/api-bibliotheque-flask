"""empty message

Revision ID: f524648d2e1e
Revises: 
Create Date: 2022-04-03 01:28:33.563835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f524648d2e1e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('libelle_categorie', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('livres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('isbn', sa.String(length=15), nullable=False),
    sa.Column('titre', sa.String(length=50), nullable=False),
    sa.Column('date_publication', sa.DateTime(), nullable=False),
    sa.Column('auteur', sa.String(length=50), nullable=False),
    sa.Column('editeur', sa.String(length=50), nullable=False),
    sa.Column('categorie_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['categorie_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('livres')
    op.drop_table('categories')
    # ### end Alembic commands ###