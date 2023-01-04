# Домашняя работа №18. Шумихин Алексей. 04.01.23

# Основной файл приложения. Здесь конфигурируется flask, сервисы, SQLAlchemy и все остальное,
# что требуется для приложения.
# Этот файл часто является точкой входа в приложение

from flask import Flask
from flask_restx import Api

from config import Config

from setup_db import db

from views.movie import movies_ns
from views.director import directors_ns
from views.genre import genres_ns


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app_):
    db.init_app(app_)
    api = Api(app_)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)


# функция создания основного объекта app
def create_app(config_object):
    app_ = Flask(__name__)
    app_.config.from_object(config_object)
    register_extensions(app_)
    return app_


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
