#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
where name matches the argument. Takes 4 arguments:
mysql username, mysql password, database name and state name searched.
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

    # Execute SQL query using user input
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(sys.argv[4])
    cursor.execute(query)

    # Fetch all rows and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()