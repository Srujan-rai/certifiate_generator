import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print("message sent")

def send_emails_from_csv(csv_file, sender_email, sender_password, subject, body_template):
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_name = row['name']
            recipient_email = row['email']
            personalized_body = body_template.format(recipient_name)
            send_email(sender_email, sender_password, recipient_email, subject, personalized_body)

# Example usage
csv_file = 'info.csv'
sender_email = 'srujanrai17@gmail.com'
sender_password = 'yufs dyox opvs bezv'
subject = 'Test Email'
body_template = 'Hello {},\n\nThis is a test email.'

send_emails_from_csv(csv_file, sender_email, sender_password, subject, body_template)
