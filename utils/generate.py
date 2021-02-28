import time
import random


def generate_session(id):
    return generate_cookie(), {
        'id': id,
        'generated-at': time.time()
    }


def generate_cookie(length=512):
    return '%030x' % random.randrange(16**(random.randint(64, length)))


def generate_id(length=32):
    return random.randint(
        int('1' + '0' * (length - 1)),
        int('9' * length)
    )
