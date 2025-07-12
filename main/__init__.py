from flask import Flask
from config import Config
from dotenv import load_dotenv
from main.extensions import db, migrate


load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = app.config.get("SECRET_KEY", "fallback_secret")

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints here if any
    from main.models.email_model import Email

    # from main.routes.routes import test_bp

    # app.register_blueprint(test_bp)


    return app
