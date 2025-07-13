import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Load template content from .html files
def get_template_content(template_name):
    path = f"main/templates/email_templates/{template_name}.html"
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

# Send email with embedded tracking pixel
def send_email_with_tracking(to_email, template_name, email_id):
    sender_email = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")

    # Load the HTML email template
    body = get_template_content(template_name)

    # Embed tracking image before </body> (or append if not found)
    tracking_url = f"http://your-domain.com/track_open?email_id={email_id}"
    tracking_img = f'<img src="{tracking_url}" width="1" height="1" />'

    html_body = body.replace("{{tracking_pixel}}", tracking_img)

    # Prepare email message
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Automated Email"
    msg["From"] = sender_email
    msg["To"] = to_email

    msg.attach(MIMEText(html_body, "html"))

    # Send using Gmail SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, to_email, msg.as_string())
