import json
import os


class Json(dict):
    def __init__(self, path, default=dict):
        self.path = path

        if not os.path.isfile(self.path):
            f = open(path, 'w')
            f.write(str(default()))
            f.close()
        
        with open(self.path, 'r') as f:
            read = json.load(f)
            for key in read:
                self[key] = read[key]
    
    def save(self):
        with open(self.path, 'r') as f:
            json.dump(self, f)

    def __setitem__(self, k, v):
        super().__setitem__(k, v)
        self.save()
    

    
