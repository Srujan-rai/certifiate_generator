from flask import Flask, request, jsonify, send_file
import pandas as pd
import cv2
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import img2pdf

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_certificates():
    cert_img = request.files['certificate']
    csv_file = request.files['csvFile']
    x_coord = int(request.form['xCoord'])
    y_coord = int(request.form['yCoord'])
    font = getattr(cv2, request.form['font'])
    sender_email = request.form['email']
    sender_password = request.form['password']
    temp_dir = 'temp'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    cert_img_path = os.path.join("temp", "certificate.png")
    cert_img.save(cert_img_path)
    base_image = cv2.imread(cert_img_path)

    df = pd.read_csv(csv_file)
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    for _, row in df.iterrows():
        name = row['name']
        email = row['email']
        img_copy = base_image.copy()
        cv2.putText(img_copy, name, (x_coord, y_coord), font, 1.6, (255, 255, 255), 2)
        output_img_path = os.path.join(output_folder, f"{name}.jpg")
        cv2.imwrite(output_img_path, img_copy)

        output_pdf_path = os.path.join(output_folder, f"{name}.pdf")
        with open(output_pdf_path, "wb") as pdf_file:
            pdf_file.write(img2pdf.convert(output_img_path))

        send_certificate(sender_email, sender_password, email, name, output_pdf_path)

    return jsonify({"message": "Certificates generated and sent successfully."})

def send_certificate(sender_email, sender_password, recipient_email, name, pdf_path):
    subject = "Participation Certificate"
    body = f"Hello {name},\nPlease find your participation certificate attached."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with open(pdf_path, 'rb') as f:
        pdf = MIMEApplication(f.read(), _subtype="pdf")
        pdf.add_header('Content-Disposition', 'attachment', filename=os.path.basename(pdf_path))
        msg.attach(pdf)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

if __name__ == '__main__':
    app.run(debug=True)
