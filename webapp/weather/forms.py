from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.fields.html5 import DateField
from datetime import datetime

class WeatherForm(FlaskForm):
    city_name = StringField("Name of city", render_kw={"class": "form-control"})
    date = DateField('date', format='%Y-%m-%d')
    submit = SubmitField('button', render_kw={"class": "btn btn-primary"})