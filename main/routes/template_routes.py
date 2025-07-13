from flask import Blueprint, jsonify
import os

template_bp = Blueprint("template", __name__)

@template_bp.route("/template", methods=["GET"])
def get_template_names():
    template_dir = "main/templates/email_templates"
    files = os.listdir(template_dir)

    templates = [f.replace(".txt", "") for f in files if f.endswith(".txt")]

    return jsonify({ "templates": templates })

@template_bp.route("/template/<name>", methods=["GET"])
def get_template_content(name):
    try:
        path = f"main/templates/email_templates/{name}.txt"
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        return jsonify({ "content": content })
    except FileNotFoundError:
        return jsonify({ "error": "Template not found" }), 404
    except Exception as e:
        return jsonify({ "error": str(e) }), 500
