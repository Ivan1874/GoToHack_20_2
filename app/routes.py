from tempfile import mktemp

from flask import redirect
from flask import render_template, send_from_directory, send_file

from app import app
from app.forms import InputForm, Mode
from .convert import zipdir
import os


@app.route('/', methods=['GET', 'POST'])
def main():
    form = Mode()
    mode = Mode().mode.data
    if form.validate_on_submit():
        return redirect('/load')
    return render_template('index.html', title='Hurt your friend!', form=form)


@app.route('/image/<emotion>')
def get_emotion(emotion):
    return send_file(os.path.join(app.root_path, f'../tmp/images/{emotion}.png'),
                     cache_timeout=0)


@app.route('/load', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        filename = mktemp()
        form.images.data.save(filename)
        zipdir(filename, 'images')
        filename2 = mktemp()
        form.audios.data.save(filename2)
        zipdir(filename2, 'audios')
        return redirect('/game')
    else:
        return render_template('load_page.html', title="Hurt your friend", form=form, image='happy')


@app.route('/game')
def game():
    return render_template('game.html')


@app.route('/static/<path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/assets/<path>')
def send_asset(path):
    return send_file(os.path.join(app.root_path, f'static/assets/{path}'), cache_timeout=0)
