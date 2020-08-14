from flask import render_template, url_for, redirect, flash, Blueprint
from utils import api_weather
from datetime import datetime, timedelta
from webapp.weather.forms import WeatherForm
import datetime

blueprint = Blueprint('weather', __name__, url_prefix='')

@blueprint.route('/process', methods=['POST'])
def process_process():
    form = WeatherForm()
    if form.validate_on_submit:
        city_name = form.city_name.data
        date = form.date.data
        now = datetime.date.today()
        if city_name == '':
            flash('Введите город')
            return redirect(url_for('weather_process'))
        if date is None:
            date = 'today'
        elif date < now:
            flash('Проверьте дату, прогноз актуален на сегодняшний день и ближайшие пять дней вперед')
            return redirect(url_for('weather_process'))
        elif date > now + timedelta(days=5):
            flash('Проверьте дату, прогноз актуален на сегодняшний день и ближайшие пять дней вперед')
            return redirect(url_for('weather_process'))
        weather = api_weather(city_name, date)
        if 'error' in weather['data']:
            flash('Проверьте город')
            return redirect(url_for('weather_process'))
        weather_today = weather['data']['current_condition'][0]['temp_C']
        weather_on_date = weather['data']['weather'][0]['maxtempC']
        if weather:
            return render_template('weather.html', weather_today = weather_today, 
                                    weather_on_date = weather_on_date, date = date, city_name = city_name)
        else:
            flash('Сервер погоды временно не доступен')
    return redirect(url_for('weather_process'))