import random

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome"


@app.route('/create')
def create():
    return "Create"


@app.route('/read/1')
def read():
    return 'Read 1'


if __name__ == '__main__':
    app.run(debug=True, port=8000)
