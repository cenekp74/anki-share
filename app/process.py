import os
import shutil
from .utils import unzip_file
from enum import Enum
import sqlite3
from flask import render_template
from app import app
import time
class ProcessingStatus(Enum):
    IN_QUEUE = 0
    STARTING_PROCESSING = 1
    UNZIPPING_ARCHIVE = 2
    GENERATING_HTML = 3
    COMPLETED = 4
    ERROR_COLLECTION_ANKI21_MISSING = 41
    ERROR_NOTES_MISSING = 42

    def error(self):
        if self.value >= 40:
            return True
        return False

def write_to_status_file(deck_id, status: ProcessingStatus):
    with open(f"instance/decks/{deck_id}/processing_status.txt", "w") as f:
        f.write(str(status.value))

def process_deck(deck_id: str):
    write_to_status_file(deck_id, ProcessingStatus.STARTING_PROCESSING)
    deck_path = f"instance/decks/{deck_id}"
    write_to_status_file(deck_id, ProcessingStatus.UNZIPPING_ARCHIVE)
    unzip_file(f"{deck_path}/anki", "deck.apkg")

    write_to_status_file(deck_id, ProcessingStatus.GENERATING_HTML)
    if not os.path.exists(f"{deck_path}/anki/collection.anki21"):
        write_to_status_file(deck_id, ProcessingStatus.ERROR_COLLECTION_ANKI21_MISSING)
        return False
    conn = sqlite3.connect(f"{deck_path}/anki/collection.anki21")
    cur = conn.cursor()
    notes = cur.execute("SELECT flds FROM notes")
    if not notes:
        write_to_status_file(deck_id, ProcessingStatus.ERROR_NOTES_MISSING)
        return False
    cards = []
    for note in notes:
        front, back = note[0].split("\x1f")
        cards.append({
            "front":front,
            "back":back,
        })
    html = render_template("deck_body.html", cards=cards)
    with open(f"{deck_path}/deck_body.html", "w", encoding="utf-8") as f:
        f.write(html)
    write_to_status_file(deck_id, ProcessingStatus.COMPLETED)
    return True