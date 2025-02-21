from . import app
import random
from celery import shared_task

def random_hex_token(length=16):
    return ''.join(random.choice('0123456789abcdef') for _ in range(length))