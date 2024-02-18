# Certificate Generator and Email Sender

This Python script generates personalized certificates with names and sends them as email attachments to the respective recipients listed in an Excel sheet.

## Prerequisites

- Python 3.x
- OpenCV (`cv2`) library
- Pandas library
- `smtplib`, `email.mime` libraries for sending emails
- Access to an SMTP server for sending emails (e.g., Gmail)

## Installation

1. Clone or download the repository to your local machine.
2. Install the required Python libraries if they are not already installed:

    ```bash
    pip install opencv-python pandas
    ```

## Usage

1. Prepare your certificate template image (`Certificate Final v2.png`). Ensure that the area where the name will be written is left blank or has placeholder text.
2. Create an Excel file (`info.xlsx`) with two columns: `name` and `email`. Enter the names and corresponding email addresses of the recipients.
3. Update the Python script (`certificate_email_sender.py`) with your Gmail credentials and file paths.
4. Run the Python script:

    ```bash
    python certificate_email_sender.py
    ```

## Configuration

- `base_image_path`: Path to the certificate template image.
- `output_folder`: Folder where the generated certificate images will be saved.
- `sender_email`: Your Gmail email address for sending emails.
- `sender_password`: Your Gmail password or an app-specific password.
- `subject`: Subject of the email.
- `body_template`: Template for the email body, which includes `{}` as a placeholder for the recipient's name.

## Notes

- Ensure that your SMTP server allows access to less secure apps or generate an app-specific password for Gmail.
- Make sure the certificate template image is properly designed with an empty space for the recipient's name.
- Verify the email addresses listed in the Excel file to avoid sending emails to incorrect addresses.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
srujan rai
