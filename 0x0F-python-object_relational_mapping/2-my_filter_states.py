#!/usr/bin/python3

"""script that takes an argument and display all values in states"""
import sys
import MySQLdb

#connect to filter state
def filter_states(username, password, database, state_name):

    #connect to db
    db = MySQLdb.connect(
        host= "localhost",
        port=3306,
        passwd=password,
        db=database
    )
    #create cursor object 
    cursor = db.cursor()

    #execute cursor
    cursor.execute("SELECT * FROM  states WHERE name = %s ORDER BY id", (state_name, ))

    #fetch the data nd print
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    #close the cursor and db
    cursor.close()
    db.close()

if __name__ == "__main__":

    if len(sys.argv) !=5:
        print("usage: ./2-filter_states.py <username> <password> <database>< state_name>")
        sys.exit(1)

    #get the command
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name =sys.argv[4]

    #call the filter
    filter_states(username, password, database, state_name)


