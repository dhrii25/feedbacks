from flask import Flask, render_template,request
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit_feedback():
    name=request.form['name']
    usn=request.form['usn']
    contact=request.form['contact']
    email=request.form['email']
    message=request.form['message']
    connection= sqlite3.connect('feedback.db')
    cursor= connection.cursor()
    cursor.execute("INSERT INTO feedback (name, usn, contact, email, message) VALUES (?, ?, ?, ?, ?);", (name, usn, contact, email, message))
    connection.commit()
    feedbacks=cursor.execute("SELECT name,message FROM feedback;").fetchall() 
    return render_template('success.html', name=name)
    connection.close()
      


if __name__ == '__main__':
    app.run(debug=True)
