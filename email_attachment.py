import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def send_email_attachment(sender_email, smtp, password, sendTO, 
                          subject, file_ways):

    receiver_email = sendTO

    message = MIMEMultipart()

    message["From"] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    file = file_ways
    attachment = open(file,'rb')

    obj = MIMEBase('application','octet-stream')

    obj.set_payload((attachment).read())
    encoders.encode_base64(obj)
    obj.add_header('Content-Disposition',
                   "attachment; filename= "+os.path.basename(file))

    message.attach(obj)

    my_message = message.as_string()
    email_session = smtplib.SMTP(smtp)
    email_session.starttls()
    email_session.login(sender_email, password)

    email_session.sendmail(sender_email,receiver_email,my_message)
    email_session.quit()
