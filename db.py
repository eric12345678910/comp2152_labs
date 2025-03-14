import sqlite3

import function

db_connection = sqlite3.connect('sqlite.db')
print("db_connection: ", db_connection)

db_cursor = db_connection.cursor()
print("db_cursor: ", db_cursor)

# Single Row
query1 = "SELECT * FROM demo"
db_cursor.execute(query1)
print("Reading 1 row:")
row = db_cursor.fetchone()
print(row)

# Multiple Rows
print("Reading 2 rows:")
rows = db_cursor.fetchmany(3)
for r in rows:
    print(r)

# All Rows
print("Reading all rows:")
#allRows = db_cursor.fetchall()
#print(allRows)
#for r in allRows:
#    print(r)
function.query_responder(db_cursor, 'fetchall')

# Insert
query2 = "INSERT INTO demo (Name, Hint) VALUES ('Eric', 'Laudrum')"
db_cursor.execute(query2)
# Use commit method on the connection
db_connection.commit()

id = input("Enter an ID: ")
query3 = "SELECT * FROM demo WHERE ID > ?"
# Pass additonal argument as a tuple
#db_cursor.execute(query3, (id))
#function.query_responder(db_cursor, 'fetchall')