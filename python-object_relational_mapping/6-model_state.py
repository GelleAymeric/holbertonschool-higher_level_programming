#!/usr/bin/python3
"""Defines the State class and links to the MySQL table 'states'."""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    """Class definition for State."""
    __tablename__ = 'states'
    
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False,
                unique=True
                )
    name = Column(String(128), nullable=False)


engine = create_engine(
    'mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa',
    echo=True
    )
Base.metadata.create_all(engine)
