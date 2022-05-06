import email
import getpass
import imaplib

user = getpass.getuser()

def email_task(orders, log, pasw, imap, email_scan, typ):
    imapObj = imaplib.IMAP4_SSL(host=imap, port=imaplib.IMAP4_SSL_PORT)
    imapObj.login(log, pasw)

    imapObj.select('INBOX', readonly=True)
    typ, data = imapObj.search(None, 'FROM', f"'{email_scan}'")

    for num in data[0].split():
        typ, data = imapObj.fetch(num, '(RFC822)')
        message = email.message_from_bytes(data[0][1])
        email_from = (f"From:{message.get('From')}")
        msg_data = (f"Date:{message.get('Date')}")
        for part in message.walk():
                if part.get_content_type() == "text/plain":
                    body_lines = part.as_string().split("\n")
                    better = "\n".join(body_lines[2:7])
                    
                    with open(orders, 'w') as file:
                        file.write(f"{email_from}\n")
                        file.write(f"{msg_data}\n")
                        file.write(f"{better}")       

    # delete email
    imapObj.select('INBOX', readonly=False) 
    typ, data = imapObj.search(None, f'FROM "{email_scan}"')
    for num in data[0].split():
        imapObj.store(num, '+FLAGS', '\\Deleted')
    
    imapObj.expunge()
    imapObj.close()
    imapObj.logout()
