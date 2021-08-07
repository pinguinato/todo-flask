"""
Flask Tutorial - creazione di una app to do list
@author Roberto Gianotto
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Home Page"


@app.route('/about')
def about():
    return "About Page"


# questo mi permette di fare run dal Pycharm
if __name__ == "__main__":
    app.run(debug=True)