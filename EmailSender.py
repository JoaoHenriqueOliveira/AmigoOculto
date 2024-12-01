import smtplib
import ssl
import os
from email.message import EmailMessage


def send_email(email_receiver=None, email_password=None, subject='Amigo Oculto Família Eh Família Ah', body='testing, cheers!'):
    email_sender = os.environ['EMAIL_OLIVEIRA']
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    content = ''
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    print(f'Email sent to {email_receiver}!')
    return


if __name__ == "__main__":
    email_receiver = input('Email receiver:')
    password = os.environ['EMAIL_OLIVEIRA_AUTH']
    send_email(email_receiver=email_receiver, email_password=password)
