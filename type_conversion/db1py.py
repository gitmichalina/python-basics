import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Track')
cur.execute('CREATE TABLE Track (title TEXT, plays INTEGER)')

cur.execute('INSERT INTO Track (title, plays) VALUES (?, ?)', ('When You Were Mine', 20))
cur.execute('INSERT INTO Track (title, plays) VALUES (?, ?)',('My Way', 15))
conn.commit()

print('Track:')
cur.execute('SELECT title, plays FROM Track')
for row in cur:
    print(row)

cur.execute('DELETE FROM Track WHERE plays < 100')
conn.commit()
print(cur.fetchall())


conn.close()
