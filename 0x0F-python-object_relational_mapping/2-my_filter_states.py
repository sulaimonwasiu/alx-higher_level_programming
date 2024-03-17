#!/usr/bin/python3
"""Filter states from database hbnt_0e_0_usa
"""
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
             WHERE name='{}'
             ORDER BY id ASC;""".format(state_filter)
    cur.execute(cmd)
    all_states = cur.fetchall()

    for state in all_states:
        if (state[1] == state_filter):
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
