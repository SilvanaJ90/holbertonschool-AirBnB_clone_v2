#!/usr/bin/python3
"""Write a script that starts a Flask web application:"""
from models import storage
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb():
    """ wep flask hbnb """
    states = storage.all(State).values()
    amenities = amenities.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
