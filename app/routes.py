from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    roles = ["Seer","Follower","Enlightened"]
    return render_template("index.html", title = "Hello!", roles = roles)
