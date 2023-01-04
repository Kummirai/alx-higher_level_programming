#!/usr/bin/python3
''' This script lists all states with a name starting with N '''

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

    ''' execute SQL queries with BINARY for byte-by-byte comparison '''
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")

    ''' fetch all-at-once '''
    rows = cur.fetchall()
    for r in rows:
        print("{}".format(r))
    cur.close()
    db.close()
