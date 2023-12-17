"""Database ORM models"""

import uuid
from typing import Optional

import sqlalchemy as sa
from sqlalchemy import orm

from .. import models as global_models

association_table = sa.Table(
    "table1_table2_mapping",
    global_models.Base.metadata,
    sa.Column("left_table_id", sa.ForeignKey("left_table.id"), primary_key=True),
    sa.Column("right_table_id", sa.ForeignKey("right_table.id"), primary_key=True),
)


class _TEMPLATE(global_models.Base):
    __tablename__ = "_TEMPLATE"

    attribute_1: orm.Mapped[str] = orm.mapped_column(nullable=False)

    foreign_m2m_rel: orm.Mapped[list["REL_TABLE"]] = orm.relationship(
        back_populates="rel_table_field_name", secondary=association_table
    )

    # Foreign Key Constraints
    """
    Explanation: SQLAlchemy requires three lines of code for a relationship. The first represents an actual column in the database (`foreign_table_id` in the example below). This is mapped as a foreign key, with dot notation referencing the actual __tablename__ of the other table and the name of the FK column (usually just `id`).
    The second line creates a relationship within SQLAlchemy. This is the `foreign_table` in the example below. In SQLAlchemy 2.0, this should be type-hinted as a list of the ORM model. To prevent circular references for M2M relationships, the name of the model can be put into quotes and SQLAlchemy will resolve at runtime. This should be a relationship that back_populates the corresponding field in the related model.
    The third and final line is in the other model (`ForeignTableORMModel` in the example below). It is a mirroring of line 2, and creates a link between the two tables. What this should look like is below:

    class ForeignTableORMModel(Base):
        _templates: Mapped[list["_TEMPLATE"]] = relationship(back_populates="foreign_table")
    """
    foreign_table_id: orm.Mapped[Optional[uuid.UUID]] = orm.mapped_column(
        sa.ForeignKey("foreign_table.id")
    )
    foreign_table: orm.Mapped[list["ForeignTableORMModel"]] = orm.relationship(
        back_populates="_templates"
    )


# ==== DUMMY DATA ==== #

DUMMY_DATA = [
    (
        _TEMPLATE,
        {
            "attribute_1": "something",
            "organisation_id": uuid.UUID("00000000-0000-0000-0000-000000000000"),
            "created_by_id": uuid.UUID("00000000-0000-0000-0000-000000000000"),
            "modified_by_id": uuid.UUID("00000000-0000-0000-0000-000000000000"),
        },
    )
]


# ==== REGISTER ==== #

MODELS_REGISTER = [_TEMPLATE]
