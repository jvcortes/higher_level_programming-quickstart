#!/usr/bin/python3
# Shows all the cities in an user-defined state
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
                    SELECT cities.name FROM
                    ((cities INNER JOIN states ON cities.state_id = states.id))
                    WHERE states.name = %(state_name)s
                    ORDER BY cities.id ASC;
                """, {'state_name': sys.argv[4]})
    rs = cur.fetchall()
    for i, record in enumerate(rs):
        if i < len(rs) - 1:
            print(record[0], end=", ")
        else:
            print(record[0])

    cur.close()
    conn.close()
