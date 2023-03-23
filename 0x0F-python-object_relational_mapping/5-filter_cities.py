#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
of a given state. Takes 4 arguments:
mysql username, mysql password, database name and state name.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    # Create cursor to execute SQL queries
    cursor = db.cursor()

    # Execute SQL query using parameterized query to prevent SQL injection
    query = """
            SELECT cities.name FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """
    cursor.execute(query, (sys.argv[4],))

    # Fetch all rows and print results
    rows = cursor.fetchall()
    print(', '.join(city[0] for city in rows))

    # Close cursor and database connection
    cursor.close()
    db.close()