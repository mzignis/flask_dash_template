from dash import Dash
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_flask_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)

    bootstrap.init_app(flask_app)
    db.init_app(flask_app)
    migrate.init_app(flask_app, db)
    login_manager.init_app(flask_app)

    from flask_app.main import bp as main_bp
    flask_app.register_blueprint(main_bp)

    from flask_app.auth import bp as auth_bp
    flask_app.register_blueprint(auth_bp)

    from flask_app.errors import bp as errors_bp
    flask_app.register_blueprint(errors_bp)

    return flask_app


def create_dash_app(flask_server, url='/dash/'):
    return Dash(__name__, server=flask_server, url_base_pathname=url)


from flask_app import models
