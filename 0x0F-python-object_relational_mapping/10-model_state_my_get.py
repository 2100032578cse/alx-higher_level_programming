#!/usr/bin/pythin3
"""script that lists all State objects from the
database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine, func
    from sqlalchemy.orm import sessionmaker

    mysql_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                                 .format(sys.argv[1], sys.argv[2],
                                         sys.argv[3]))
    Base.metadata.create_all(mysql_engine)
    Session = sessionmaker(bind=mysql_engine)
    session = Session()
    ele= session.query(State).filter(
        State.name == func.binary(sys.argv[4])).first()
    if ele:
        print("{:d}".format(ele.id))
    else:
        print("Not found")
