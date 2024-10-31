#!/usr/bin/python3
"""Start link class to table in database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """ Class definition for State """
    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                primary_key=True,
                unique=True,
                nullable=False
                )
    name = Column(String(128), nullable=False)


engine = create_engine(
    'mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa'
    )
Base.metadata.create_all(engine)
