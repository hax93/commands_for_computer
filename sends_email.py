import smtplib


def send_email(sendTO, text_subject, text):

    email = f'{sendTO}'
    # login email
    smtpObj = smtplib.SMTP('smtp' 999)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('xyz@xyz.com', 'password')

    # send email
    body = f'Subject: {text_subject} \n{text}'
    print('Send email %s...' % email)
    sendmailStatus = smtpObj.sendmail('denka.hera@onet.pl', email, body)
    if sendmailStatus != {}:
        print('There was a problem sending e-mail to the address: %s',  email)
    smtpObj.quit()
