import time
import random

def generate_session(id):
    return generate_cookie(), {
        'id': id,
        'generated-at': time.time()
    }

def generate_cookie(l=512, m=64):
    return '%030x' % random.randrange(16**(random.randint(64, l)))
