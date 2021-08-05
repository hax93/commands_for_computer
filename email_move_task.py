"""every 15minutes check inbox, and value emails
move to tasks.txt"""
import imapclient
import pyzmail
import sys
import time

filename = 'task/tasks.txt' #directory txt tasks

def imap_login(login, password, imap, focus_email):

        time.sleep(900)
        imapObj = imapclient.IMAPClient(imap, ssl=True)
        imapObj.login(login, password)

        imapObj.select_folder('INBOX', readonly=True)   #select folder 'INBOX'

        messages = imapObj.search(['FROM', focus_email]) #script follow one e-mail

        for msgid, data in imapObj.fetch(messages, ['ENVELOPE']).items():   #get emails from inbox
            envelope = data[b'ENVELOPE']

            rawMessages = imapObj.fetch(messages, ['BODY[]'])

            mess = pyzmail.PyzMessage.factory(rawMessages[msgid][b'BODY[]'])
            sys.stdout = open(filename, 'w', encoding="UTF-8")    #start copy/paste value from emails to takss.txt

            print(f"{mess.get_subject()}")
            print(f"{mess.text_part.get_payload().decode(mess.text_part.charset)}")
            sys.stdout.close()

        imapObj.select_folder('INBOX',
                              readonly=False)  # delete email(move to trash) with task, readonly need 'False'
        imapObj.delete_messages(messages)
        imapObj.expunge()
        imapObj.logout()
