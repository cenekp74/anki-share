from app import app, db
from flask import flash, render_template, redirect, url_for, jsonify, abort, request, send_file, send_from_directory
from werkzeug.utils import secure_filename
from .utils import random_hex_token, is_valid_deck_id
from .celery_tasks import start_deck_processing
import os
from .db_classes import Deck
from .process import ProcessingStatus

@app.route('/favicon.ico')
def send_favicon():
    return send_from_directory('static/img', 'favicon.ico')

@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('upload'))

@app.route('/upload', methods=["POST", "GET"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    
    file = request.files.get('filepond')
    filename = secure_filename(file.filename)
    if not filename.endswith(".apkg"):
        abort(400)
    deck_id = random_hex_token()
    
    os.mkdir(f"instance/decks/{deck_id}")
    os.mkdir(f"instance/decks/{deck_id}/anki")
    file.save(f"instance/decks/{deck_id}/anki/deck.apkg")

    start_deck_processing.delay(deck_id)
    deck = Deck(
        id = deck_id,
        name = filename.removesuffix(".apkg").replace("_", " ")
    )
    db.session.add(deck)
    db.session.commit()
    return deck_id

@app.route('/deck/<deck_id>')
def deck(deck_id):
    if not is_valid_deck_id(deck_id): abort(400)
    deck = Deck.query.get(deck_id)
    if not deck: abort(404)

    deck_path = f"instance/decks/{deck.id}"
    if not os.path.exists(deck_path): abort(500)
    
    status = ProcessingStatus.IN_QUEUE
    if os.path.exists(f"{deck_path}/processing_status.txt"):
        with open(f"{deck_path}/processing_status.txt") as status_file:
            status = ProcessingStatus(int(status_file.read()))

    if status is ProcessingStatus.COMPLETED:
        deck_body = open(f"{deck_path}/deck_body.html", "r", encoding="utf-8").read()
        return render_template("deck.html", deck_body=deck_body, deck_name=deck.name, deck_id=deck_id)
    
    if status.error():
        error = "Unexpected server error"
        if status is ProcessingStatus.ERROR_COLLECTION_ANKI21_MISSING:
            error = "collection.anki21 not found in apkg. Please make sure the deck has been exported from a recent anki version."
        elif status is ProcessingStatus.ERROR_NOTES_MISSING:
            error = "No notes were found in your apkg file. Please make sure that there are cards in the deck. Only 2 filed cards with text/images are supported."
        elif status is ProcessingStatus.ERROR_PROCESSING_NOTES:
            error = "'fields parsing error' Currently only decks with 2 basic fields are supported. Sorry for the inconvenience."
        elif status is ProcessingStatus.ERROR_UNPACKING_ARCHIVE:
            error = "Error while upacking .apkg archive"
        elif status is ProcessingStatus.ERROR_PROCESSING_MEDIA_FILE:
            error = "Error while processing anki 'media' file. Please try exporting the deck with support for older versions."
        return render_template("deck.html", error=error)
    return render_template("deck.html", deck_body="Your deck is currently being processed. It should take no longer then a few minutes. Please reload to page to update.")

@app.route('/deck/<deck_id>/browse')
def browse_deck(deck_id):
    if not is_valid_deck_id(deck_id): abort(400)
    deck = Deck.query.get(deck_id)
    if not deck: abort(404)

    deck_path = f"instance/decks/{deck.id}"
    if not os.path.exists(deck_path): abort(500)
    
    if os.path.exists(f"{deck_path}/processing_status.txt"):
        with open(f"{deck_path}/processing_status.txt") as status_file:
            status = ProcessingStatus(int(status_file.read()))
    if not status is ProcessingStatus.COMPLETED: abort(400)
    
    deck_body = open(f"{deck_path}/deck_body.html", "r", encoding="utf-8").read()
    return render_template("browse_deck.html", deck_body=deck_body, deck_name=deck.name, deck_id=deck_id)

@app.route('/deck/<deck_id>/download')
def download_deck(deck_id):
    if not is_valid_deck_id(deck_id): abort(400)
    deck = Deck.query.get(deck_id)
    if not deck: abort(400)

    deck_path = f"instance/decks/{deck.id}"
    if not os.path.exists(f"{deck_path}/anki/deck.apkg"): abort(400)
    return send_file(f"../{deck_path}/anki/deck.apkg", download_name=f"{deck.name}.apkg")

@app.route('/deck/<deck_id>/media/<filename>')
def send_deck_media(deck_id, filename):
    if not is_valid_deck_id(deck_id): abort(400)
    deck = Deck.query.get(deck_id)
    if not deck: abort(400)
    return send_from_directory(f"../instance/decks/{deck.id}/media", filename)