#!/usr/bin/python3
# Shows all the cities alongside its states.
if __name__ == "__main__":
    import sys
    import MySQLdb

    conn = MySQLdb.connect(host="localhost",
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)

    cur = conn.cursor()

    cur.execute("""
                    SELECT cities.id, cities.name, states.name FROM
                    ((cities INNER JOIN states ON cities.state_id = states.id))
                    ORDER BY cities.id, states.name ASC;
                """)
    rs = cur.fetchall()
    for record in rs:
        print(record)

    cur.close()
    conn.close()
