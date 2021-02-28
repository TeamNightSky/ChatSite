import time
import random

def generate_session(id):
    return generate_cookie(), {
        'id': id,
        'generated-at': time.time()
    }

def generate_cookie(l=512, m=64):
    return '%030x' % random.randrange(16**(random.randint(64, l)))

def generate_id(l=32):
    return random.randint(
        int('1' + '0' * (l-1)),
        int('9' * l)
    )