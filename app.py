from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connecton():
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connecton()
    todos = conn.execute('select * from todos').fetchall()
    conn.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['post'])
def add():
    todo = request.form['todo']
    conn = get_db_connecton()
    conn.execute('insert into todos (task) values (?)', (todo,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connecton()
    conn.execute('delete from todos where id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    conn = get_db_connecton()
    conn.execute('create table if not exists todos (id integer primary key, task text)')
    conn.close()
    app.run(debug=True)