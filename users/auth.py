import hashlib
import secrets
from utils.storage import CONFIG, PASSWORDS



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

