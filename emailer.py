import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(sender_email, sender_password, receiver_email, pdf_path):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Swiggy Weekly Analytics Report'
    
    body = """
    Hi Team,
    
    Please find attached this week's Swiggy Analytics report.
    
    Key insights included:
    - Top 10 cities by revenue
    - Top 10 restaurants performance
    - Category wise analysis
    - Monthly revenue trend
    
    For any queries, please contact the Analytics Team.
    
    Regards,
    Analytics Team
    """

    msg.attach(MIMEText(body, 'plain'))


    # Attach PDF
    with open(pdf_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 
                       f'attachment; filename=SwiggyBI_Report.pdf')
        msg.attach(part)
    logging.info("PDF attached to email!")


    # Send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        logging.info("Email sent successfully!")
    except Exception as e:
        logging.error(f"Email failed: {e}")