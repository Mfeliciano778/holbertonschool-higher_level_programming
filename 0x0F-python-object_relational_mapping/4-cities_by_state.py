#!/usr/bin/python3
'''Task 4'''
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cmd = "SELECT cities.id, cities.name, states.name \
          FROM cities LEFT JOIN states \
          ON cities.state_id = states.id \
          ORDER BY id ASC;"
    cur.execute(cmd)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
