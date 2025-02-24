from . import app
import random
import zipfile
import os
import pyzstd

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
    zip_path = os.path.join(path, zip_filename)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.namelist():
            member_path = os.path.abspath(os.path.join(path, member))
            if not member_path.startswith(os.path.abspath(path) + os.sep):
                raise Exception("Unsafe file path detected")
        zip_ref.extractall(path)

def decompress_pyzstd(input_path, output_path):
    with open(input_path, 'rb') as compressed_file:
        compressed_data = compressed_file.read()
        decompressed_data = pyzstd.decompress(compressed_data)

    with open(output_path, 'wb') as decompressed_file:
        decompressed_file.write(decompressed_data)