import cv2
import os
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with open(attachment_path, 'rb') as attachment:
        image = MIMEImage(attachment.read(), name=os.path.basename(attachment_path))
        msg.attach(image)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

df = pd.read_csv('info.csv')  
base_image_path = "Certificate v4.png"
base_image = cv2.imread(base_image_path)

output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

thickness = 3
font = cv2.FONT_HERSHEY_COMPLEX
colour = (0, 0, 0)
font_scale = 1.3

for index, row in df.iterrows():
    name = str(row['name'])
    email = str(row['email'])

    img_to_text = base_image.copy()
    cv2.putText(img_to_text, name, (790, 855), font, font_scale, colour, thickness)

    output_image_path = os.path.join(output_folder, f"{name}.jpg")
    cv2.imwrite(output_image_path, img_to_text)

    subject = 'Certificate Attached'
    body = f'Hello {name},\n\nThank you for joining us at the Surya Namaskar practice on Ratha Saptami. Your presence added value to the event, and we appreciate your dedication to health and well-being.\n\nPlease find your certificate attached.'

    send_email(sender_email='yogaparticipationcertificate@gmail.com',
               sender_password='gvnq hnio yfhv rrkm',
               recipient_email=email,
               subject=subject,
               body=body,
               attachment_path=output_image_path)

    print(f"Certificate for {name} has been sent to {email}")

print("All certificates sent successfully")
