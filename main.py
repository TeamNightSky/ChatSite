import time
import importlib
from utils.stats import total_files, total_lines, total_chars
from auth.auth import Login
from utils.storage import CONFIG, SESSIONS

from flask import Flask, render_template, request


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
    return None


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



"""API"""
API_ROUTES = {
    "/v1/auth": [
        "auth.auth", 
        "auth_endpoint"
    ]
}

for route, item in API_ROUTES.items():
    path, endpoint = item
    module = importlib.import_module(path)

    @app.route('/api' + route)
    def api(*a, **kw):
        return getattr(module, endpoint)(request, *a, **kw)


if __name__ == '__main__':
    print('Files:', total_files())
    print('Lines:', total_lines())
    print('Characters:', total_chars())
    app.run('0.0.0.0', 8080)
