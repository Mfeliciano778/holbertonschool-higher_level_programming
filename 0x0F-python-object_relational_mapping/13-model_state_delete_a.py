#!/usr/bin/python3
"""Start link class to table in database
"""
import sys

from sqlalchemy.orm.session import Session
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    stat = session.query(State).filter(State.name.like("%a%")).all()

    for state in stat:
        session.delete(state)
    session.commit()
    session.close()
