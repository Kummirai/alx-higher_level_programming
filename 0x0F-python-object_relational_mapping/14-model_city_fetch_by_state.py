#!/usr/bin/python3
'''
Script that prints all City objects from the database hbtn_0e_6_usa
'''

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    ''' create an instance of Engine=core interface to the database '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    '''pool_pre_ping tests connections for liveness upon each checkout'''

    ''' create a session '''
    session = sessionmaker(bind=engine)()

    ''' work with session to change object name '''
    result = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for state, city in result:
        print("{}: ({:d}) {}".format(state.name, city.id, city.name))
    session.close()
