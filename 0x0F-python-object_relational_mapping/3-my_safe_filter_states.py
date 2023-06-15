#!/usr/bin/python3
"""
This script is safe from MySQL injections and takes in an argument and
displays all values in the states where `name` matches the argument
from the database `hbtn_0e_0_usa`."""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the DB and get the states
    from the DB.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE %(name)s
            ORDER BY
                id ASC
        """, {
            'name': argv[4]
        })

        tuples = cur.fetchall()

    if tuples is not None:
        for tuplee in tuples:
            print(tuplee)
