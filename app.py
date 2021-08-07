"""
Flask Tutorial - creazione di una app to do list
@author Roberto Gianotto
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')

# questo mi permette di fare run dal Pycharm


if __name__ == "__main__":
    app.run(debug=True)