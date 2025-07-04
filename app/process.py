import os
import shutil
from .utils import unzip_file, decompress_pyzstd, clean_html
from enum import Enum
import sqlite3
from flask import render_template
from app import app
import json
import re
import random

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
    ERROR_PROCESSING_MEDIA_FILE = 45

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
    compressed = False # whether the apkg file is from a new anki version that uses protocol buffers and zstd compression
    if os.path.exists(f"{deck_path}/anki/collection.anki21b"):
        decompress_pyzstd(f"{deck_path}/anki/collection.anki21b", f"{deck_path}/anki/collection.anki21")
        compressed = True
    if not os.path.exists(f"{deck_path}/anki/collection.anki21"): # if there is no collection.anki21b and no collection.anki21 files, it means the deck is version < 2.1
        if os.path.exists(f"{deck_path}/anki/collection.anki2"):
            shutil.move(f"{deck_path}/anki/collection.anki2", f"{deck_path}/anki/collection.anki21")
    if not os.path.exists(f"{deck_path}/anki/collection.anki21"):
        write_to_status_file(deck_id, ProcessingStatus.ERROR_COLLECTION_ANKI21_MISSING)
        return False
    conn = sqlite3.connect(f"{deck_path}/anki/collection.anki21")
    cur = conn.cursor()

    models = json.loads(list(cur.execute("SELECT models FROM col"))[0][0]) # dict of card types (models)
    notes = list(cur.execute("SELECT flds FROM notes"))
    note_mids = list(cur.execute("SELECT mid FROM notes"))
    if not notes:
        write_to_status_file(deck_id, ProcessingStatus.ERROR_NOTES_MISSING)
        return False
    try:
        cards = []
        reversed_cards = [] # separate list that will be appended to the end of cards
        for (note, mid) in zip(notes, note_mids):
            mid = mid[0]
            front = note[0].split("\x1f")[0]
            front = clean_html(front)
            if len(note[0].split("\x1f")) == 1:
                back = ""
            else:
                back = note[0].split("\x1f")[1]
                back = clean_html(back)
            cards.append({
                "front":front,
                "back":back,
            })

            if models[str(mid)]["name"] == "Basic (and reversed card)":
                reversed_cards.append({
                    "front":back,
                    "back":front,
                })
            if "optional reversed card" in models[str(mid)]["name"]: # if the card type has something to do with optional reversed card, the third field usually indicates whether reverse should be included
                if len(note[0].split("\x1f")) >= 3:
                    if "y" in note[0].split("\x1f")[2].lower():
                        reversed_cards.append({
                            "front":back,
                            "back":front,
                        })
        cards += reversed_cards
    except Exception as _e:
        write_to_status_file(deck_id, ProcessingStatus.ERROR_PROCESSING_NOTES)
        return False
    
    html = render_template("deck_body.html", cards=cards)

    write_to_status_file(deck_id, ProcessingStatus.PROCESSING_MEDIA)
    os.makedirs(f"{deck_path}/media", exist_ok=True)

    try:
        if compressed: # if the anki deck is from a newer version, the media file is encoded using protocol buffers, so it needs to be handled differently
            from .anki_proto import import_export_pb2
            with open(f"{deck_path}/anki/media", "rb") as f:
                media_data = f.read()
            media_entries = import_export_pb2.MediaEntries()
            media_entries.ParseFromString(media_data)
            images_dict = {}
            for index, entry in enumerate(media_entries.entries):
                images_dict[str(index)] = entry.name
        else:
            images_dict = json.load(open(f"{deck_path}/anki/media"))
    except Exception as _e:
        write_to_status_file(deck_id, ProcessingStatus.ERROR_PROCESSING_MEDIA_FILE)

    for filename, image_name in images_dict.items():
        if not os.path.exists(f"{deck_path}/anki/{filename}"): continue
        shutil.move(f"{deck_path}/anki/{filename}", f"{deck_path}/media/{filename}")
        html = html.replace(image_name, f"/deck/{deck_id}/media/{filename}")
    
    if compressed: # if the anki deck is from a newer version, the media files are copmressed using zstd
        for filename in os.listdir(f"{deck_path}/media"):
            decompress_pyzstd(f"{deck_path}/media/{filename}", f"{deck_path}/media/{filename}")

    # cloze format
    cloze_pattern = re.compile(r"{{c\d+::(.*?)}}")
    def replace_cloze(match):
        return f'<span class="cloze" onclick="this.classList.toggle(\'revealed\');event.stopPropagation()">{match.group(1)}</span>'
    html = cloze_pattern.sub(replace_cloze, html)

    audio_pattern = re.compile(r"\[sound:([^\]]+)\]")
    def replace_audio(match):
        return f'<audio controls src="{match.group(1)}"></audio>'
    html = audio_pattern.sub(replace_audio, html)

    with open(f"{deck_path}/deck_body.html", "w", encoding="utf-8") as f:
        f.write(html)
    write_to_status_file(deck_id, ProcessingStatus.COMPLETED)
    return True