from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    return render_template("index.html")

@main_bp.route("/template_content/<name>")
def template_content(name):
    try:
        return render_template(f"email_templates/{name}.html")
    except:
        return "<p>Template not found.</p>"
