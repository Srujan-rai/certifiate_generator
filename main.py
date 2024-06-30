import cv2
import os
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

import img2pdf

def send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with open(attachment_path, 'rb') as attachment:
        if attachment_path.endswith('.jpg') or attachment_path.endswith('.png'):
            image = MIMEImage(attachment.read(), name=os.path.basename(attachment_path))
            msg.attach(image)
        elif attachment_path.endswith('.pdf'):
            attachment_data = attachment.read()
            pdf = MIMEApplication(attachment_data, _subtype="pdf")
            pdf.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))
            msg.attach(pdf)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

not_sent_log = "not_sent.txt"
if os.path.exists(not_sent_log):
    os.remove(not_sent_log)
df = pd.read_csv('info.csv')
base_image_path = "participation.png"
base_image = cv2.imread(base_image_path)

output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

point = (100, 595)
font_scale = 1.6
colour = (255, 255, 255)
thickness = 2
font = cv2.FONT_HERSHEY_TRIPLEX

for index, row in df.iterrows():
    name = str(row['name'])
    email = str(row['email'])

    img_to_text = base_image.copy()
    cv2.putText(img_to_text, name, (790, 855), font, font_scale, colour, thickness)

    output_image_path = os.path.join(output_folder, f"{name}.jpg")
    cv2.imwrite(output_image_path, img_to_text)

    output_pdf_path = os.path.join(output_folder, f"{name}.pdf")
    with open(output_pdf_path, "wb") as f:
        f.write(img2pdf.convert(output_image_path))

    subject = 'Participation Certificate for Devhost 2024'
    body = (
        f'Hello {name},\n\n'
        f'Thank you for your participation in Devhost 2024, held from June 14-16 at Sahyadri College of Engineering and Management. '
        f'Your participation played a significant role in making this event a success.\n\n'
        f'Please find your participation certificate attached.\n\n'
        f'To help us improve our future events, we kindly request you to fill out a short feedback form by clicking the link below:\n\n'
        f'https://forms.gle/WANnmUkDHUSRuLHv6\n\n'
        f'We look forward to your feedback and seeing you at future events.\n\n'
        f'Best regards,\n'
        f'Sahyadri Open Source Community'
    )
    try:
        send_email(sender_email='sankalp.sosc@sahyadri.edu.in',
                   sender_password='tdvd jdfv jnxv buhf',
                   recipient_email=email,
                   subject=subject,
                   body=body,
                   attachment_path=output_pdf_path)
        print(f"Certificate for {name} has been sent to {email}")
    except Exception as e:
        print(f"Failed to send certificate to {email}. Error: {str(e)}")
        with open(not_sent_log, 'a') as log_file:
            log_file.write(f"{name}, {email}\n")

print("All certificates sent successfully")
