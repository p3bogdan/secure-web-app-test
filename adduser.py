import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
# Replace 'username' and 'password' with desired values
c.execute("INSERT INTO users (username, password) VALUES ('testuser', 'testpassword')")
conn.commit()
conn.close()

