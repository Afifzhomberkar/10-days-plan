from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_users():
    users = [
        {'name': 'Alice', 'age': 22},
        {'name': 'Bob', 'age': 17},
        {'name': 'Charlie', 'age': 25}
    ]
    info = {
        'group': 'Python Learners',
        'count': len(users)
    }
    return render_template("users.html", users=users, info=info)

if __name__ == '__main__':
    app.run(debug=True)
