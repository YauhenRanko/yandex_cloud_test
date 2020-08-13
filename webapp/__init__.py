from flask import Flask, render_template, url_for, request, redirect, flash
from webapp.weather.forms import WeatherForm
from webapp.weather.views import blueprint as weather_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.register_blueprint(weather_blueprint)

    @app.route('/')
    def weather_process():
        form = WeatherForm()
        return render_template('index.html', form = form)

    return app
    
    


