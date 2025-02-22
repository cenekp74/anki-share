from app import app, db
from flask import flash, render_template, redirect, url_for, jsonify, abort, request, send_file, send_from_directory
from werkzeug.utils import secure_filename
from .utils import random_hex_token
from .celery_tasks import start_deck_processing
import os
from .db_classes import Deck

@app.route('/favicon.ico')
def send_favicon():
    return send_from_directory('static/img', 'favicon.ico')

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

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