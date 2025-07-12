from main import create_app
from main.extensions import db
from main.models.email_model import Email  

app = create_app()

with app.app_context():
    # Insert sample email entries
    email1 = Email(
        recipient_email="alice@example.com",
        template_used="welcome_template.html",
        status="Not Sent"
    )
    email2 = Email(
        recipient_email="bob@example.com",
        template_used="promo_template.html",
        status="Sent"
    )

    # Commit to database
    db.session.add_all([email1, email2])
    db.session.commit()

    # Verify: Print all email records
    emails = Email.query.all()
    for e in emails:
        print(f"📧 ID: {e.id}, To: {e.recipient_email}, Template: {e.template_used}, Status: {e.status}")
