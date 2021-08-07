"""
Flask Tutorial - creazione di una app to do list
@author Roberto Gianotto
"""

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    return render_template('base.html')

# questo mi permette di fare run dal Pycharm


if __name__ == "__main__":
    # creo il db
    db.create_all()
    # run dell'app
    app.run(debug=True)