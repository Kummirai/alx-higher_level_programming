#!/usr/bin/python3
'''
Contains the class definition of State
and an instance Base = declarative_base()
'''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

''' instance of module; used for defining mapped classes '''
Base = declarative_base()


class City(Base):
    ''' Class definition for State which inherits from Base '''
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
