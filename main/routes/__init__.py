from flask import Blueprint

main = Blueprint('main', __name__)

from .email_routes import email_bp

main.register_blueprint(email_bp)