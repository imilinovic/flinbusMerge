import string
import random


def gen_id() -> str:
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
