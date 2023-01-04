#!/usr/bin/python3
'''
Displays all values in the states table of hbtn_0e_0_usa where name
matches argument passed to script
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

    ''' execute SQL queries with BINARY for byte-by-byte comparison '''
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}'\
    ORDER BY id".format(argv[4]))

    ''' fetch all-at-once '''
    rows = cur.fetchall()
    for r in rows:
        print("{}".format(r))
    cur.close()
    db.close()
