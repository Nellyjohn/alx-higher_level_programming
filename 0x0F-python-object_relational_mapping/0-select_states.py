#!/usr/bin/python3
""" This module lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    query = "SELECT * FROM states ORDER BY states.id"
    cur.execute(query)

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    conn.close()
