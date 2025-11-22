import sqlite3

connection= sqlite3.connect('students.db')
cursor= connection.cursor()
cmd="""
CREATE TABLE IF NOT EXISTS students (
    usn INTEGER PRIMARY KEY ,
    name TEXT NOT NULL,
    branch CHAR(10) NOT NULL,
    semester TEXT NOT NULL,
    cgpa INTEGER NOT NULL
    );
"""
cursor.execute(cmd)
connection.commit()
cmd="INSERT INTO students ( usn,name, branch, semester, cgpa) VALUES (?, ?, ?, ?, ?);"
cursor.execute(cmd, ( 1001,'Emily Davis', 'CSE', '5th', 8))
cursor.execute(cmd, ( 1002,'Michael Wilson', 'ECE', '6th', 7))
cursor.execute(cmd, ( 1003,'Sarah Miller', 'ME', '4th', 9))
connection.commit()
s=cursor.execute("SELECT * FROM students;").fetchall()
print(s)
r=cursor.execute("SELECT * FROM students WHERE name='Sarah Miller';").fetchall()
print(r)
connection.close()