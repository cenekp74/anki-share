from app import app
from flask import flash, render_template, redirect, url_for, jsonify, abort, request, send_file, send_from_directory
from werkzeug.utils import secure_filename
from app.utils import random_hex_token
import os

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
    token = random_hex_token()
    
    os.mkdir(f"instance/decks/{token}")
    os.mkdir(f"instance/decks/{token}/anki")
    file.save(f"instance/decks/{token}/anki/deck.apkg")

    return token