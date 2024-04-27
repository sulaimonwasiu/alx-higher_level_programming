#!/usr/bin/python3
""" List all cities from the database
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
    cmd = """SELECT cities.id, cities.name, states.name
             FROM states
             INNER JOIN cities ON states.id = cities.state_id
             ORDER BY cities.id ASC"""

    cur.execute(cmd)
    all_cities = cur.fetchall()

    for state in all_cities:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
