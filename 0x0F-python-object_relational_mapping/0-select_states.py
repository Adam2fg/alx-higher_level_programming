#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)
    
    # Create cursor object
    cursor = db.cursor()

    # Execute query to fetch all states from database
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows and print them in the desired format
    for row in cursor.fetchall():
        print(row)
    
    # Close cursor and database connection
    cursor.close()
    db.close()