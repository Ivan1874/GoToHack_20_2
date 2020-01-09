import json
import os
from shutil import rmtree
from tempfile import mktemp

from flask import redirect
from flask import render_template, send_from_directory, send_file

from app import app
from app.forms import InputForm, Mode
from .convert import unzip
from app.ai import ai


@app.route('/', methods=['GET', 'POST'])
def main():
    form = Mode()
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
        unzip_path = os.path.join(app.root_path, f'../tmp/images/')
        converted_path = os.path.join(app.root_path, f'../tmp/converted/')
        unzip(filename, unzip_path)

        if os.path.isdir(converted_path):
            rmtree(converted_path)
        os.mkdir(converted_path)
        res = ai(os.listdir(unzip_path), unzip_path, converted_path)
        with open(os.path.join(converted_path, 'data.json'), 'w') as f:
            f.write(json.dumps(res))
        # filename2 = mktemp()
        # form.audios.data.save(filename2)
        # unzip(filename2, os.path.join(app.root_path, f'../tmp/audios/'))
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


@app.route('/imgassets/<path>')
def send_imgasset(path):
    return send_file(os.path.join(app.root_path, f'../tmp/converted/{path}'), cache_timeout=0)
