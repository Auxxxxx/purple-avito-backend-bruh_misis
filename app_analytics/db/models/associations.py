from sqlalchemy import Table, Column, ForeignKey, Integer

from db.db import Base


user_item = Table(
    "user_item",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("item_id", ForeignKey("item.id"), unique=True),
)

baseline1 = Table(
    "baseline_matrix_1",
    Base.metadata,
    Column("id", Integer),
    Column("microcategory_id", ForeignKey("microcategory.id")),
    Column("location_id", ForeignKey("location.id")),
    Column("price", Integer)
)

discount1 = Table(
    "discount_matrix_1",
    Base.metadata,
    Column("id", Integer),
    Column("microcategory_id", ForeignKey("microcategory.id")),
    Column("location_id", ForeignKey("location.id")),
    Column("price", Integer)
)

discount2 = Table(
    "discount_matrix_2",
    Base.metadata,
    Column("id", Integer),
    Column("microcategory_id", ForeignKey("microcategory.id")),
    Column("location_id", ForeignKey("location.id")),
    Column("price", Integer)
)

discount3 = Table(
    "discount_matrix_3",
    Base.metadata,
    Column("id", Integer),
    Column("microcategory_id", ForeignKey("microcategory.id")),
    Column("location_id", ForeignKey("location.id")),
    Column("price", Integer)
)