from . import app
import random
import shutil
import os

def random_hex_token(length=16):
    return ''.join(random.choice('0123456789abcdef') for _ in range(length))

def unzip_file(path, zip_filename) -> None:
    """
    unpacks zip file to its parent directory
    """
    shutil.unpack_archive(os.path.join(path, zip_filename), path, "zip")