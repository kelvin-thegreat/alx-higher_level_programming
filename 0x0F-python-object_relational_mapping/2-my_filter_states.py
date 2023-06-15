#!/usr/bin/python3
"""
Script that list all states from the DB `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Provide the MySQL username, password, and database name as command-line arguments
    Access to the database and get the states
    from the database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE '{}' \
                 ORDER BY id ASC".format(argv[4]))
    tuples = cur.fetchall()

    for tuplee in tuples:
        print(tuplee)

