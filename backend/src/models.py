"""Base model classes for all models in the application."""

import datetime as dt
import uuid

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy import sql as sa_sql




class Base(orm.DeclarativeBase):
#     """Base class for all models in the application."""

#     id: orm.Mapped[uuid.UUID] = orm.mapped_column(
#         primary_key=True,
#         nullable=False,
#         default=uuid.uuid4, # Set a default value using "default="
#     )


#     datetime_modified: orm.Mapped[dt.datetime] = orm.mapped_column(
#         nullable=False,
#         server_default=sa_sql.func.now(),
#     )


#     datetime_created: orm.Mapped[dt.datetime] = orm.mapped_column(
#         nullable=False,
#         server_default=sa_sql.func.now(),
#     )

# ## use scenario?
#     def __getitem__(self, key):
#         return getattr(self, key)

#     def __setitem__(self, key, value):
#         return setattr(self, key, value)

#     def __contains__(self, key):
#         return hasattr(self, key)

#     def keys(self):
#         items = self.__mapper__.attrs.keys()
#         return items

#     def get(self, key, default=None):
#         if hasattr(self, key):
#             return getattr(self, key)
#         return default

#     def items(self):
#         return [(key, getattr(self, key)) for key in self.keys()]

#     def values(self):
#         return [getattr(self, key) for key in self.keys()]

#     def __iter__(self):
#         return iter(self.keys())
    


# ### 字典式访问方法：

# # __getitem__ 和 __setitem__ 方法允许你像操作字典那样通过键值来获取和设置属性。
# # __contains__ 方法用来检查一个键是否存在于模型属性中。
# # keys 方法返回模型所有属性的键。
# # get 方法获取指定键的值，如果键不存在则返回默认值。
# # items 方法返回键值对的列表。
# # values 方法返回所有属性值的列表。
# # __iter__ 方法使得模型实例可迭代，迭代的是属性键。