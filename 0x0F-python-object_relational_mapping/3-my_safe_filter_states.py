#!/usr/bin/python3
"""This module takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument, one safe from injections"""

import MySQLdb
from sys import argv
import sys

if __name__ == "__main__":
    """Access to the database and get the states
        from the database."""

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s ORDER \
                 BY states.id ASC", {'name': argv[4]})
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
