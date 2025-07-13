from flask import Flask
from main.routes.routes import main_bp  # ✅ Corrected Import

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app
