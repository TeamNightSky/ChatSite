import hashlib
import secrets
from utils.storage import Json
from flask import Request
import time

PASSWORDS = Json("data/passwords.json")
CONFIG = Json("config.json")


class Login:
    def __init__(self, user_id):
        self.user_id = user_id
        self.hash = hashlib.sha256(PASSWORDS.get(str(user_id)).encode("utf-8")).hexdigest()
        self.active_hash, self.active_rand = self.generate_hash()

    @property
    def _rand(self):
        return secrets.token_hex(CONFIG["auth-rand-length"])


    def generate_hash(self):
        r = self._rand
        return hashlib.sha256((self.hash + r).encode("utf-8")).hexdigest(), r

sessions = []

def auth_endpoint(request: Request):
    json = request.get_json()
    try:
        user_id = json["user-id"]
    except KeyError:
        return {"success": False, "error": "User id was not found."}

    time.sleep(0.01)


    login = Login(user_id)
    sessions.append(login)
    return {"rand": login.active_rand, "success": True}

