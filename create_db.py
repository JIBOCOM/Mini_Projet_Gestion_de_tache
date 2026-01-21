import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Sample users (passwords are plain-text for simplicity; in production, hash them with e.g., werkzeug.security)
cur.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ('admin', 'adminpass', 'admin'))
cur.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ('user1', 'userpass', 'user'))

# Sample books
cur.execute("INSERT INTO books (title, author, available) VALUES (?, ?, ?)", ('The Great Gatsby', 'F. Scott Fitzgerald', 1))
cur.execute("INSERT INTO books (title, author, available) VALUES (?, ?, ?)", ('1984', 'George Orwell', 1))
cur.execute("INSERT INTO books (title, author, available) VALUES (?, ?, ?)", ('To Kill a Mockingbird', 'Harper Lee', 0))  # Borrowed example

connection.commit()
connection.close()
