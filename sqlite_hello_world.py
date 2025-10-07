# sqlite_hello_world.py

import sqlite3


with sqlite3.connect("./users.db") as con:
    cur = con.cursor()
    res = cur.execute("SELECT * FROM users")

    for record in res:
        print (record)

# con.close() is implicitly called from here

