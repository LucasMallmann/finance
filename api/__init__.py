from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migration import Migrate
from config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app=app)
    migrate.inita_app(app)

    from api.main.routes import main
    app.register_blueprint(main)

    return app
