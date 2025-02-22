from . import app
import random
import shutil
import os

def random_hex_token(length=16):
    return ''.join(random.choice('0123456789abcdef') for _ in range(length))

def is_valid_deck_id(deck_id: str) -> bool:
    """
    function that checks if given string is a valid deck_id. it only checks the format, NOT if the deck is in database
    """
    if not len(deck_id) == 16: return False
    for ch in deck_id:
        if ch not in '0123456789abcdef': return False
    return True

def unzip_file(path, zip_filename) -> None:
    """
    unpacks zip file to its parent directory
    """
    shutil.unpack_archive(os.path.join(path, zip_filename), path, "zip")