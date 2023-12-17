"""Database service module."""

from collections import namedtuple
from inspect import signature

import sqlalchemy as sa
from pydantic.types import constr

QueryStr = constr(regex=r"^[ -~]+$", min_length=1)

BooleanFunction = namedtuple(
    "BooleanFunction", ("key", "sqlalchemy_fn", "only_one_arg")
)
BOOLEAN_FUNCTIONS = [
    BooleanFunction("or", sa.or_, False),
    BooleanFunction("and", sa.and_, False),
    BooleanFunction("not", sa.not_, True),
]


class Operator(object):
    """Operator class for SQLAlchemy filter operators."""

    OPERATORS = {
        "is_null": lambda f: f.is_(None),
        "is_not_null": lambda f: f.isnot(None),
        "==": lambda f, a: f == a,
        "eq": lambda f, a: f == a,
        "!=": lambda f, a: f != a,
        "ne": lambda f, a: f != a,
        ">": lambda f, a: f > a,
        "gt": lambda f, a: f > a,
        "<": lambda f, a: f < a,
        "lt": lambda f, a: f < a,
        ">=": lambda f, a: f >= a,
        "ge": lambda f, a: f >= a,
        "<=": lambda f, a: f <= a,
        "le": lambda f, a: f <= a,
        "like": lambda f, a: f.like(a),
        "ilike": lambda f, a: f.ilike(a),
        "not_ilike": lambda f, a: ~f.ilike(a),
        "in": lambda f, a: f.in_(a),
        "not_in": lambda f, a: ~f.in_(a),
        "any": lambda f, a: f.any(a),
        "not_any": lambda f, a: sa.func.not_(f.any(a)),
    }

    def __init__(self, operator=None):
        if not operator:
            operator = "=="

        if operator not in self.OPERATORS:
            raise Exception(
                f"Operator `{operator}` not valid."
            )  # TODO - custom exception

        self.operator = operator
        self.function = self.OPERATORS[operator]
        self.arity = len(signature(self.function).parameters)
