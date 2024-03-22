#!/usr/bin/python3
""" script that takes in the name of a state as an argument and list
all cities of that state, using the database hbtn_0e_4_usa"""

import sys
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT cities.name FROM cities LEFT JOIN states\
            ON states.id = cities.state_id WHERE states.name = %s\
            ORDER BY states.id ASC", (sys.argv[4],))
    ans = c.fetchall()
    res = len(ans)
    for i in range(res):
        if i < res - 1:
            print(ans[i][0], end=", ")
        else:
            print(ans[i][0])
