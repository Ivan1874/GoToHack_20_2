from app import app
from flask import render_template, send_from_directory


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/2')
def index2():
    return render_template('index2.html')


@app.route('/3')
def index3():
    return render_template('index3.html')


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
