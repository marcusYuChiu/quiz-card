from flask import Flask


from .cards import views as card_views
from .extensions import db, migrate


def create_app(config_object="quiz_card.settings"):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    app.register_blueprint(card_views.blueprint)
    return None
