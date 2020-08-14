from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.fields.html5 import DateField
from datetime import datetime

class WeatherForm(FlaskForm):
    city_name = StringField("Ведите название города", render_kw={"class": "form-control"})
    date = DateField('Выберите дату', format='%Y-%m-%d')
    submit = SubmitField('Получит прогноз', render_kw={"class": "btn btn-primary"})