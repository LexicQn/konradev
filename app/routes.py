import flask
from app import app
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template("index.html", title = "Hello!")
