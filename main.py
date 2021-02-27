from utils.storage import Json
from flask import Flask, render_template


app = Flask(__name__)

users = Json('data/users.json')
posts = Json('data/posts.json')

config = Json('config.json')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/explore')
def explore():
    return render_template('explore.html')


@app.route('/faq')
def faq():
    return render_template('help.html')


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/posts')
def posts():
    return render_template('allposts.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
