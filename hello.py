from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)


@app.route("/")
def index():
    return 'Index Paage'

@app.route("/pTag")
def hello_world_p_tag():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/hello")
def hello_world():
    return 'Hello World'

@app.route('/users/<username>')
def show_user_name(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/projects/') # Wont produce 404 with trailing slah.
def projects():
    return 'The projects page'

@app.route('/about') # Will produce 404 if /about/ is called
def about():
    return 'The about page'

@app.route("/")