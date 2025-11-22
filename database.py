import sqlite3

connection = sqlite3.connect('feedback.db')
cursor = connection.cursor()
cmd = """
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    usn varchar(10) NOT NULL,
    contact varchar(10) NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL
    );
"""
cursor.execute(cmd)
connection.commit()

cmd = "Insert INTO feedback (name, usn, contact, email, message)VALUES (?, ?, ?, ?, ?);" 
cursor.execute(cmd, ('John Doe', '1RV17CS001', '9876543210', 'john.doe@example.com', 'Great service!'))
cursor.execute(cmd, ('Jane Smith', '1RV17CS002', '8765432109', 'jane.smith@example.com', 'Very helpful!'))
cursor.execute(cmd, ('Alice Johnson', '1RV17CS003', '7654321098', 'alice.johnson@example.com', 'Excellent support!'))
cursor.execute(cmd, ('Bob Brown', '1RV17CS004', '6543210987', 'bob.brown@example.com', 'Quick response!'))
connection.commit()

f=cursor.execute("SELECT * FROM feedback;").fetchall()
print(f)
connection.close()