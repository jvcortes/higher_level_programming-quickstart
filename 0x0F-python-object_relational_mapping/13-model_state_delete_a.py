#!/usr/bin/python3
# Deletes all the state objects which have the letter a inside their names.
# by the user
if __name__ == "__main__":
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    session.query(State).filter(
        State.name.like("%a%")).delete(synchronize_session=False)
    session.commit()

    session.close()
