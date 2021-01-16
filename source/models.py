from flask_sqlalchemy import SQLAlchemy, BaseQuery
from sqlalchemy import Table, Text, Integer, String, Column


Base = BaseQuery

class Employee(Base):
    __tablename__ = Table(
        "employee",
        Column('id', Integer, primaru_key=True),
        Column("name", String),
        Column("first_name", String(50)),
        Column("last_name", String(50)),
        Column("position", String),
        Column("salary", Integer)

    )

