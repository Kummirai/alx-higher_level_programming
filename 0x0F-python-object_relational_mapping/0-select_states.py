#!/usr/bin/python3
''' This script lists all states from the database hbtn_0e_usa '''

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
    cur.execute("SELECT * FROM states ORDER BY id")

    ''' fetch all-at-once '''
    rows = cur.fetchall()
    for col in rows:
        print("{}".format(col))
    cur.close()
    db.close()
