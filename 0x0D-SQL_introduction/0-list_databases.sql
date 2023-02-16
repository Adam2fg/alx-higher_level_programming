#!/bin/bash

# Set MySQL credentials
MYSQL_USER="your_mysql_username"
MYSQL_PASSWORD="your_mysql_password"

#Get a list of all databases in the MySQL server
databases=$(mysql -u $MYSQL_USER -p$MYSQL_PASSWORD -e "SHOW DATABASES;" | grep -Ev "(Database|information_schema|performance_schema)")

# Print the list of databases
echo "List of databases:"
echo "$databases"
