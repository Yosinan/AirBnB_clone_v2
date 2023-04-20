# importing flask
from flask import Flask

app = Flask(__name__)

# app decorator for routing
@app.route('/')
def hello():
    return 'Hello HBNB!'
