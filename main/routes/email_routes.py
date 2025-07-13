from flask import Blueprint, request, jsonify
from main.extensions import db
from main.models.email_model import Email
from main.utils import send_email_with_tracking
from flask import send_file

email_bp = Blueprint("email", __name__)

@email_bp.route("/emails", methods=["GET"])
def get_emails():
    emails = Email.query.all()
    email_list = [{"id": email.id, "recipient_email": email.recipient_email, "status": email.status} for email in emails]  
    return jsonify(email_list), 200

@email_bp.route("/send_email", methods=["POST"])
def send_email_route():
    data = request.get_json()
    email_id = data.get("email_id")
    template = data.get("template_name")

    if not email_id or not template:
        return jsonify({"success": False, "error": "Missing fields"}), 400

    email = Email.query.get(email_id)
    if not email:
        return jsonify({"success": False, "error": "Email not found"}), 404

    try:
        send_email_with_tracking(email.recipient_email, template, email.id)

        email.status = "SENT"
        db.session.commit()

        return jsonify({"success": True, "message": "Email sent"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


from flask import send_file

@email_bp.route("/track_open")
def track_open():
    email_id = request.args.get("email_id")
    if email_id:
        email = Email.query.get(email_id)
        if email:
            email.status = "OPENED"
            db.session.commit()

    return send_file("main/static/1x1.png", mimetype="image/png")

