#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """ du must use storage for fetching data from the storage """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
