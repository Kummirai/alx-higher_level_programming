#!/usr/bin/python3
'''
Script that lists all cities in state that's passed in as argument
from the database hbtn_0e_4_usa
'''

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    ''' connects to the database '''
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    ''' cursor for multiple separate working envs thru one connection '''
    cur = db.cursor()

    ''' execute SQL queries '''
    cur.execute("\
    SELECT * FROM cities JOIN states\
    ON cities.state_id = states.id WHERE states.name = %s\
    ORDER BY cities.id ASC", (argv[4],))

    ''' fetch all-at-once '''
    rows = cur.fetchall()
    print(", ".join([row[2] for row in rows]))
    cur.close()
    db.close()
