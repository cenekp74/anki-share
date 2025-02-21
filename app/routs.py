from app import app
from flask import flash, render_template, redirect, url_for, jsonify, abort, request, send_file, send_from_directory
from werkzeug.utils import secure_filename

@app.route('/favicon.ico')
def send_favicon():
    return send_from_directory('static/img', 'favicon.ico')

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")