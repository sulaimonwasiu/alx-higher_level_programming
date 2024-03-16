#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database):
    # Connect to the MySQL server
    conn = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to execute queries
    cursor = conn.cursor()

    # Execute the query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Display the states
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    # Get the MySQL username, password, and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to list states
    list_states(username, password, database)