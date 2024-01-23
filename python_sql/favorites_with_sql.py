import sqlite3

db_connection = sqlite3.connect('favorites.db')
cursor = db_connection.cursor()


# rows = cursor.execute("SELECT * FROM favorites WHERE problem = 'Mario'").fetchall()
rows = cursor.execute("SELECT COUNT(*) FROM favorites WHERE problem = 'Mario'").fetchall()
# if there is no matches, it will be empty list

for row in rows:
    print(row[0])

# to use variables in sql queries, ? is a placeholder.
favorite = ('Speller',)
rows = cursor.execute("SELECT COUNT(*) FROM favorites WHERE problem = ?", favorite).fetchall()

for row in rows:
    print(row[0])