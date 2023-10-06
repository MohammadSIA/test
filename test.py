import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define your email details
email_address = "mamad.sia@hotmail.com"
email_password = "Visa1402"
recipient_email = "mamad.siaa@gmail.com"
email_subject = "Appointment Request for Student Visa Application"
email_body = """Dear Sir/Madam,

I am writing to formally request an appointment at the Embassy of Italy in Tehran for the explicit purpose of submitting my student visa application. I have been admitted to University of Padova and consequently require a national visa for my entry.

Below are the personal details of Afsaneh Poshkooei:

Full Name: Afsaneh Poshkooei
Passport number: H53405151
Institution: Università degli Studi di PADOVA
Course: ICT for Internet and multimedia
ID Summary: 231524
Beginning of Classes: 02/10/2023
Phone number: +989309743342

I humbly request your esteemed office to kindly arrange an appointment for me at your earliest convenience. I remain at your disposal to visit the embassy at your discretion, available on any day and at any time that aligns with your scheduling preferences.

Your time and assistance are greatly appreciated, and I earnestly anticipate your prompt response.

Sincerely,
"""

# Set up the SMTP server for Outlook/Hotmail
smtp_server = "smtp-mail.outlook.com"
smtp_port = 587

# Create the email message
msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = recipient_email
msg['Subject'] = email_subject

# Attach the email body
msg.attach(MIMEText(email_body, 'plain'))

# Establish the SMTP connection and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, recipient_email, msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {str(e)}")
