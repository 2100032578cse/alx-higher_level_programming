#!/usr/bin/python3
""" these lists all states from the database hbtn_0e_0_us"""

import sys
import MySQLdb
if __name__ = "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states where name LIKE
              BINARY '{}' ORDER BY states.id ASC".format(sys.argv[4]))
    i = c.fetchall()
    for i in rows:
        print(i)
