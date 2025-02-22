import os
import shutil
from .utils import unzip_file
from enum import Enum
import sqlite3

class ProcessingStatus(Enum):
    STARTING_CONVERSION = 0
    UNZIPPING_ARCHIVE = 1
    ERROR_COLLECTION_ANKI21_MISSING = 41

def write_to_status_file(deck_id, status: ProcessingStatus):
    with open(f"instance/decks/{deck_id}/processing_status.txt", "w") as f:
        f.write(str(status.value))

def process_deck(deck_id: str):
    write_to_status_file(deck_id, ProcessingStatus.STARTING_CONVERSION)
    deck_path = f"instance/decks/{deck_id}"
    write_to_status_file(deck_id, ProcessingStatus.UNZIPPING_ARCHIVE)
    unzip_file(f"{deck_path}/anki", "deck.apkg")

    if not os.path.exists(f"{deck_path}/anki/collection.anki21"):
        write_to_status_file(deck_id, ProcessingStatus.ERROR_COLLECTION_ANKI21_MISSING)

    conn = sqlite3.connect(f"{deck_path}/anki/collection.anki21")
    cur = conn.cursor()
    notes = cur.execute("SELECT flds FROM notes")