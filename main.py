import time

from utils.stats import total_files, total_lines, total_chars
from utils.storage import CONFIG, SESSIONS
from utils.generate import generate_session

from flask import Flask, render_template, request, redirect


app = Flask(__name__)

def get_userid_from_cookie():
    if CONFIG['userCookie'] in request.cookies:
        cookie = request.cookies.get(CONFIG['userCookie'])
        if cookie is not None and cookie in SESSIONS:
            session = SESSIONS[cookie]
            if time.time() > session['last_updated'] + CONFIG['cookieTimeout']:
                SESSIONS.deletekey(cookie)
            else:
                return session['id']

def set_userid_to_cookie(id):
    cookie, session = generate_session(id)
    SESSIONS[cookie] = session
    return session


@app.route('/')
def home():
    userid = get_userid_from_cookie()
    if userid is None:
        return redirect('/login')
    return render_template('index.html', config=CONFIG)


@app.route('/login')
def login():
    return render_template('login.html', config=CONFIG)

@app.route('/register')
def register():
    return render_template('register.html', config=CONFIG)

@app.route('/messages')
def messages():
    return render_template('messages.html', config=CONFIG)


@app.route('/explore')
def explore():
    return render_template('explore.html', config=CONFIG)


@app.route('/faq')
def faq():
    return render_template('help.html', config=CONFIG)


@app.route('/post')
def post():
    return render_template('post.html', config=CONFIG)


@app.route('/posts')
def posts():
    return render_template('allposts.html', config=CONFIG)


@app.route('/api/v1/auth')
def authorize():
    pass


if __name__ == '__main__':
    print('Files:', total_files())
    print('Lines:', total_lines())
    print('Characters:', total_chars())
    app.run('0.0.0.0', 8080)
