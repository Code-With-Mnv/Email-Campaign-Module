from flask import Flask
from config import Config
from dotenv import load_dotenv

from main.extensions import db, migrate
from main.routes.email_routes import email_bp
from main.routes.template_routes import template_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = app.config.get("SECRET_KEY", "fallback_secret")

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(email_bp)
    app.register_blueprint(template_bp)

    return app
