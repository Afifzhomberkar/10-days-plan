from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# DB setup
def init_db():
    conn = sqlite3.connect('students.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT
        )
    ''')
    conn.close()

init_db()

@app.route('/')
def home():
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    conn.close()
    return render_template('home.html', students=students)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    age = request.form['age']
    grade = request.form['grade']
    conn = sqlite3.connect('students.db')
    conn.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('students.db')
    conn.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/edit/<int:id>')
def edit(id):
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE id=?", (id,))
    student = cur.fetchone()
    conn.close()
    return render_template('edit.html', student=student)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']
    age = request.form['age']
    grade = request.form['grade']
    conn = sqlite3.connect('students.db')
    conn.execute("UPDATE students SET name=?, age=?, grade=? WHERE id=?", (name, age, grade, id))
    conn.commit()
    conn.close()
    return redirect(url_for('home.html'))

if __name__ == '__main__':
    app.run(debug=True)
