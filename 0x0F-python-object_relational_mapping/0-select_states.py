#!/usr/bin/python3
# Lists all the states
if __name__ == "__main__":
    import sys
    import MySQLdb

    conn = MySQLdb.connect(host="localhost",
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    rs = cur.fetchall()
    for record in rs:
        print(record)

    cur.close()
    conn.close()
