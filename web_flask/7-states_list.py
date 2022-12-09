#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ du must use storage for fetching data from the storage """
    states = storage.all("State")
    states = [state for state in states.values()]
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def close():
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
