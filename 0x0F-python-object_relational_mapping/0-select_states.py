#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
                )

        cur = conn.cursor()
        cur.execute("SELECT * FROM states OREDER BY id ASC")

        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))
        sys.exit(1)
