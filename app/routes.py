from app import app
from flask import render_template, send_from_directory, send_file


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game')
def index():
    return render_template('game.html')


@app.route('/static/<path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/assets/<path>')
def send_asset(path):
    return send_file(f'/media/fox/D/_Progr/_Python/GoToHack_20_2/app/static/assets/{path}', cache_timeout=0)
