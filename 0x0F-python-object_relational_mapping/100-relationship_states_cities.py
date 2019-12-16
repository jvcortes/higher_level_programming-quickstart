#!/usr/bin/python3
# Adds a new state object containing a city object
# by the user
if __name__ == "__main__":
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.exc import SQLAlchemyError
    from model_state import Base, State
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    try:
        state = State(name='California')
        city = City(name='San Francisco')
        state.cities.extend([city])
        session.add(state)
        session.add(city)
        session.commit()
    except SQLAlchemyError as ex:
        print(ex)

    session.close()
