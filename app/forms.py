from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField, HiddenField, RadioField
from wtforms.validators import DataRequired

from app import app

app.jinja_env.globals['bootstrap_is_hidden_field'] = lambda field: isinstance(field, HiddenField)


class InputForm(FlaskForm):
    images = FileField('Фото: ', validators=[DataRequired()])
    # audios = FileField('Аудио: ')
    submit = SubmitField('Далее!')


class Mode(FlaskForm):
    # mode = RadioField(validators=[DataRequired()], choices=[('standart', 'Standart'), ('bdsm', 'BDSM')])
    button = SubmitField('Ок')
