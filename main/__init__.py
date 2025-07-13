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

    from main.models.email_model import Email

    from main.routes import main as main_blueprint
    from main.routes.template_routes import template_bp
    app.register_blueprint(main_blueprint)
    app.register_blueprint(template_bp)

    return app
