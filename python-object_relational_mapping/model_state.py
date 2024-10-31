#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """ Class definition for State """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    
    