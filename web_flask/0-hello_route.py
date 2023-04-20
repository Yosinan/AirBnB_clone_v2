# importing flask
from flask import Flask

app = Flask(__name__)

# app decorator for routing
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'
