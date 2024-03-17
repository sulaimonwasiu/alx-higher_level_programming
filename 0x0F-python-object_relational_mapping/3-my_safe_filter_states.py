#!/usr/bin/python3
# List all states where 'name' matches the argument
# But this time, one safe from MySQL injection.
# Username, password, database name, and state name given as user args
import MySQLdb
import sys


def list_states(username, password, database, state_filter):
    """List all states from database hbnt_0e_0_usa
    """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    cur = db.cursor()
    cmd = """SELECT *
             FROM states
             WHERE name LIKE %s
             ORDER BY id ASC;"""
    cur.execute(cmd, ('{}%'.format(state_filter),))
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
    state_filter = sys.argv[4]

    list_states(username, password, database, state_filter)
