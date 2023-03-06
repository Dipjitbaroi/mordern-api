import sqlite3
conn = sqlite3.connect("books.sqlite")

cursor = conn.cursor()
cursor.execute("""CREATE TABLE book (
   id integer PRIMARY KEY,
   author text,
   language text,
   title text
   )""")