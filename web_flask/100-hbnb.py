#!/usr/bin/python3
'''
    script that starts a Flask web application:
'''

from flask import Flask, render_template

# importing storage, state & Amenity

from models import storage
from models.state import State
from models.place import Place
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def tearDown(self):
    ''' remove the current SQLAlchemy Session '''
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnbFilters():
    ''' lists States, places and amenities '''
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    places = list(storage.all(Place).values())


    return render_template(
        '100-hbnb.html',
        states=states,
        amenities=amenities,
        places=places)


if __name__ == '__main__':
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
