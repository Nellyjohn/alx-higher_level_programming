#!/usr/bin/python3
"""This module  lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv
import sys

if __name__ == "__main__":
    """Access to the database and get the states
        from the database."""

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[1], db=sys.argv[3], charset="utf8")
    cur = conn.cursor
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'
                ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
