#!/usr/bin/python3
'''Task 4'''
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    state = argv[4]
    cur = db.cursor()
    cmd = "SELECT cities.id, cities.name, states.name \
          FROM cities LEFT JOIN states \
          ON cities.state_id = states.id \
          ORDER BY id ASC;"
    cur.execute(cmd)
    query_rows = cur.fetchall()
    new_list = []
    for row in query_rows:
        if row[2] == state:
            new_list.append(row[1])
    for item in range(0, len(new_list)):
        if item == len(new_list) - 1:
            print(new_list[item], end="")
        else:
            print(new_list[item], end=", ")
    print("")
    cur.close()
    db.close()
