#!/usr/bin/python3

"""
script that list all the state starting with N(upper N)
"""
import sys
import MySQLdb

"""CONNECT to my filter state"""

def filter_states(username, password, database):
    """connect to mysql database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    #create the cursor object object
    cursor = db.cursor()

    #to execute the query
    cursor.execute("SELECT * FROM  states WHERE name LIKE 'N%' ORDER BY id")

    #fetch the data nd print
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    #close the cursor and db
    cursor.close()
    db.close()

if __name__ == "__main__":

    if len(sys.argv) !=4:
        print("usage: ./1-filter_states.py <username><password><database>")
        sys.exit(1)

    #get the command
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]


    #call the filter
    filter_states(username, password, database)



