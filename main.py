import random
import time

from utils.storage import Json
from utils.stats import total_files, total_lines, total_chars
from auth.auth import Login

from flask import Flask, render_template, request


app = Flask(__name__)

CONFIG = Json('config.json')
SESSIONS = Json('data/sessions.json')


def get_userid_from_cookie():
    if CONFIG['userCookie'] in request.cookies:
        cookie = request.cookies.get(CONFIG['userCookie'])
        if cookie is not None and cookie in SESSIONS:
            session = SESSIONS[cookie]
            if time.time() > session['last_updated'] + CONFIG['cookieTimeout']:
                del SESSIONS[cookie]
            else:
                return session['id']
    return None

def generate_session(id):
    return generate_cookie(), {
        'id': id,
        'generated-at': time.time()
    }

def generate_cookie(l=512, m=64):
    return '%030x' % random.randrange(16**(random.randint(64, l)))


@app.route('/login')
def login():
    return 'Login Page'


@app.route('/')
def home():
    return render_template('index.html', config=CONFIG)


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



"""API""" # I think this should work
API_ROUTES = {"/v1/auth": "auth.auth auth_endpoint"}

for route, path in API_ROUTES.items():
    module = __import__(path.split(" ")[0])
    @app.route(route)
    def api(*a, **kw):
        return getattr(module, path.split(" ")[-1])(request, *a, **kw)


if __name__ == '__main__':
    print('Files:', total_files())
    print('Lines:', total_lines())
    print('Characters:', total_chars())
    app.run('0.0.0.0', 8080)
