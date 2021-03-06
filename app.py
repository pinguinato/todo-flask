"""
Flask Tutorial - creazione di una app to do list
@author Roberto Gianotto
"""

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    details = db.Column(db.String(255))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    # show all todos
    todo_list = Todo.query.all()
    return render_template('base.html', todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    # aggiunta di un nuovo task
    title = request.form.get("title")
    additional_details = request.form.get("details")
    new_todo = Todo(title=title, details=additional_details, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    # aggiorna un task
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    # rimuove un task
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


# questo mi permette di fare run dal Pycharm
if __name__ == "__main__":
    # creo il db
    db.create_all()
    # run dell'app
    app.run(debug=True)