Project Name: 0x0F. Python - Object-relational mapping
Tools Used: Python, OOP, SQL, MySQL, ORM, SQLAlchemy

0-select_states.py
Question
0. Get all states
Breakdown of solution: The code is a Python script that connects to a MySQL database and retrieves a list of US states from a table called "states". The script takes three arguments as input: a MySQL username, a MySQL password, and the name of the database.

The script then uses the MySQLdb module to connect to the MySQL database running on the local machine at port 3306. Once connected, it creates a cursor object that can execute SQL queries on the database. The script then executes an SQL query to select all rows from the "states" table and sorts them by the "id" column in ascending order.
Finally, the script iterates through the results of the SQL query and prints each row to the console. Each row represents a state and includes two values: an ID number and the name of the state.
The script closes the cursor and database connection after printing the results to the console. 