#!/usr/bin/python3
"""Filter states from database hbnt_0e_0_usa
"""
import MySQLdb
import sys


def list_states(username, password, database):
    """List all states from database hbnt_0e_0_usa
    """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    cur = db.cursor()
    cur.execute("SELECT DISTINCT id, name FROM states WHERE name like 'N%' ORDER BY id ASC")
    all_states = cur.fetchall()

    for state in all_states:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
