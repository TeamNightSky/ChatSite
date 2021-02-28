import json
import os


class Json(dict):
    def __init__(self, path, default=dict):
        self.path = path

        if not os.path.isfile(self.path):
            f = open(path, 'w')
            f.write(str(default()))
            f.close()

        f = open(self.path, 'r')
        if len(f.readlines()) == 0:
            f.close()
            with open(self.path, 'w') as f:
                f.write(str(default()))
        else:
            f.close()

        with open(self.path, 'r') as f:
            read = json.load(f)
            for key in read:
                super().__setitem__(key, read[key])

    def save(self):
        with open(self.path, 'r') as f:
            json.dump(self, f, indent=4)

    def __setitem__(self, k, v):
        super().__setitem__(k, v)
        self.save()

    def deletekey(self, k):
        del self[k]
        self.save()


CONFIG = Json('config.json')
SESSIONS = Json('data/sessions.json')
PASSWORDS = Json("data/passwords.json")
