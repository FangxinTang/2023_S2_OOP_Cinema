"""Helper functions and classes for the backend."""

import dataclasses
import enum
import re
from typing import Any, Self, Type


class NoriaEnum(enum.Enum):
    def __new__(cls, *values):
        obj = object.__new__(cls)

        # first value is none - handled in __init__
        obj._value_ = values[0]
        if len(values) > 1:
            for other_value in values[1:]:
                cls._value2member_map_[other_value] = obj
        obj._all_values = values
        return obj

    def __repr__(self):
        return "<%s.%s: %s>" % (
            self.__class__.__name__,
            self._name_,
            ", ".join([repr(v) for v in self._all_values]),
        )

    def __json__(self):
        return str(self)

    def __str__(self) -> str:
        return self.name

    def convert(self, value: str) -> str:
        """Convert a value to the enum"""
        raise NotImplementedError

    def __eq__(self, other):
        if isinstance(other, str):
            other = re.sub(r"[\s\-]", "_", other.lower()).strip()
            return other in self._all_values
        else:
            return super().__eq__(other)

    def __hash__(self):
        return hash(self.name)

    @classmethod
    def find_alias(cls, alias: str) -> str | None:
        """Find the alias for the unit. Safer way to access the alias than `cls('alias')`."""
        alias_cleaned = re.sub(r"[\s\-]", "_", alias.lower()).strip()
        try:
            val = cls(alias_cleaned)
            return val
        except ValueError:
            return None


@dataclasses.dataclass
class NoriaDataclass:
    """Base class for composite column dataclasses."""

    def __init__(
        self,
        *args,
    ):
        raise NotImplementedError()

    def __dict__(self):
        return dataclasses.asdict(self)

    def __getitem__(self, key):
        return dataclasses.asdict(self)[key]

    def __setitem__(self, key, value):
        dataclasses.asdict(self)[key] = value

    def __contains__(self, key):
        return key in self.keys()

    def keys(self):
        return dataclasses.asdict(self).keys()

    def get(self, key, default=None):
        return dataclasses.asdict(self).get(key, default)

    def items(self):
        return dataclasses.asdict(self).items()

    def values(self):
        return dataclasses.asdict(self).values()

    def __iter__(self):
        return dataclasses.asdict(self).__iter__()

    # def __len__(self):
    #     return len(tuple(self))

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__()}>"

    def __tuple__(self):
        return tuple(self.__dict__().values())

    def __eq__(self, other):
        if isinstance(other, dict):
            return self.__dict__() == other

        return self.__dict__() == other.__dict__()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__tuple__())

    def __composite_values__(self):
        raise NotImplementedError()

    def from_tuple(cls, value: tuple):
        return cls(*value)

    def __str__(self):
        return str(dict(self))

    def __json__(self):
        return dict(self)
