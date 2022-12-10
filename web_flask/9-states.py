#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)

@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states_cities(state_id=None):
    """ du must use storage for fetching data from the storage """
    states = storage.all(State)
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
