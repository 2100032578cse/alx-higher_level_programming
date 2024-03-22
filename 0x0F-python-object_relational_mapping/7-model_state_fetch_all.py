#!/usr/bin/python3
"""script that lists all State objects from the
database hbtn_0e_6_usa"""

if __name__=="__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker


    mysql_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1],sys.argv[2],sys.argv[3]))
    Base.metadata.create_all(mysql_engine)
    Session = sessionmaker(bind=mysql_engine)
    session = Session()
    for item in session.query(State).order_by(State.id):print("{:d}: {:s}".format(item.id, item.name))
