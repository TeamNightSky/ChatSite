from utils.storage import Json
from flask import Flask, render_template


app = Flask(__name__)

users = Json('data/users.json')
posts = Json('data/posts.json')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/explore')
def explore():
    pass


@app.route('/faq')
def faq():
    pass


@app.route('/post')
def post():
    pass


@app.route('/posts')
def posts():
    pass


if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
