from datetime import datetime
from main.extensions import db

class Email(db.Model):
    __tablename__ = 'emails'

    id = db.Column(db.Integer, primary_key=True)
    recipient_email = db.Column(db.String(255), nullable=False)
    template_used = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(50), default='Not Sent')  # Not Sent, Sent, Opened
    sent_at = db.Column(db.DateTime, nullable=True)
    opened_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<Email to {self.recipient_email}, Status: {self.status}>"
