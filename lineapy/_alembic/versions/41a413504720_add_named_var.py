"""add named var

Revision ID: 41a413504720
Revises: 38d5f834d3b7
Create Date: 2022-07-06 14:14:42.354458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "41a413504720"
down_revision = "38d5f834d3b7"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "assigned_variable_node",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("variable_name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", "variable_name"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("assigned_variable_node")
    # ### end Alembic commands ###