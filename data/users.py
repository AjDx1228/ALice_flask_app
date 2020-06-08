import sqlalchemy
from .db_session import SqlAlchemyBase

from sqlalchemy import orm


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    ip = sqlalchemy.Column(sqlalchemy.String, nullable=True)