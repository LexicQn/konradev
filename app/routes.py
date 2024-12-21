from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    roles = ["Seer","Follower","Enlightened"]
    print(roles)
    return render_template("index.html", title = "Hello!", roles = roles)
