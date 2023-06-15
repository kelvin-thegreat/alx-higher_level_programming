#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that
state, using the database `hbtn_0e_4_usa`.

"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Database Connection and getting the cities
    from the database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""

        SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE %(state_name)s
        ORDER BY cities.id ASC

        """, {
            'state_name': argv[4]
        })

        cities = cur.fetchall()

    if cities is not None:
        print(", ".join([city[1] for city in cities]))
