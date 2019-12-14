#!/usr/bin/python3
# Filters the states by the user input
if __name__ == "__main__":
    import sys
    import MySQLdb

    conn = MySQLdb.connect(host="localhost",
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)

    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
                 ORDER BY id ASC;".format(sys.argv[4]))
    rs = cur.fetchall()
    for record in rs:
        print(record)

    cur.close()
    conn.close()
