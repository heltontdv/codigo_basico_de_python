import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)")
cursor.execute("INSERT INTO usuarios (nome) VALUES ('João')")
conn.commit()

cursor.execute("SELECT * FROM usuarios")
print(cursor.fetchall())

conn.close()
