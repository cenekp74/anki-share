import os
import shutil
from .utils import unzip_file
from enum import Enum
import sqlite3
from flask import render_template
from app import app
import json

class ProcessingStatus(Enum):
    IN_QUEUE = 0
    STARTING_PROCESSING = 1
    UNZIPPING_ARCHIVE = 2
    GENERATING_HTML = 3
    PROCESSING_MEDIA = 4
    COMPLETED = 20
    ERROR_COLLECTION_ANKI21_MISSING = 41
    ERROR_NOTES_MISSING = 42
    ERROR_PROCESSING_NOTES = 43
    ERROR_UNPACKING_ARCHIVE = 44

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
    try:
        unzip_file(f"{deck_path}/anki", "deck.apkg")
    except Exception as e:
        write_to_status_file(deck_id, ProcessingStatus.ERROR_UNPACKING_ARCHIVE)
        return False

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
    try:
        cards = []
        for note in notes:
            front, back = note[0].split("\x1f")
            cards.append({
                "front":front,
                "back":back,
            })
    except Exception as _e:
        write_to_status_file(deck_id, ProcessingStatus.ERROR_PROCESSING_NOTES)
        return False
    html = render_template("deck_body.html", cards=cards)

    write_to_status_file(deck_id, ProcessingStatus.PROCESSING_MEDIA)
    os.makedirs(f"{deck_path}/media", exist_ok=True)
    images_json = json.load(open(f"{deck_path}/anki/media"))
    for filename, image_name in images_json.items():
        if not os.path.exists(f"{deck_path}/anki/{filename}"): continue
        shutil.move(f"{deck_path}/anki/{filename}", f"{deck_path}/media/{filename}")
        html = html.replace(image_name, f"/deck/{deck_id}/media/{filename}")
        
    with open(f"{deck_path}/deck_body.html", "w", encoding="utf-8") as f:
        f.write(html)
    write_to_status_file(deck_id, ProcessingStatus.COMPLETED)
    return True