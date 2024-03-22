#!/usr/bin/python3
"""script that lists all State objects from the
database hbtn_0e_6_usa"""

if __name__=="__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker


    engine = create_engine()
