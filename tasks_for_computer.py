import os
import glob
import getpass
import logging
from email_attachment import send_email_attachment
from settings_db import hash_db, results

"""
example email:
    subject: None
    content: password
             show | download
             txt | text.txt
"""
user = getpass.getuser()

logging.basicConfig(filename=f'c:\\Users\\{user}\\Documents\\backup\\log.log',
                    encoding='utf-8', level=logging.DEBUG, 
                    format='%(asctime)s [%(levelname)s] %(message)s')

def check_words(orders, result, folder_scan):
    try:
        # if you want more EXTENSION just add below e.g. ,xml
        EXTENSION = "*,txt,docx,doc,xlsx,pdf"
        data = []
        show = 'show'        
        download = 'download'

        with open(orders, 'r+', encoding="UTF-8") as file_object:
            file = file_object.read()
            lines = file.split('\n')

            if hash_db(lines[3]) == results('hash', 2) and show in file:

                command = lines[5]
                search = command
                if search in EXTENSION:
                    #   scan and try result output to results.txt
                    os.chdir(folder_scan)   
                    for direct in glob.glob(f'*.{search}'):
                        data.append(direct)

                    my_string = ""

                    for i in data:
                        my_string += (f'{i} \n')
           
                    with open(result, 'w', encoding='utf-8') as files:
                        files.write(my_string)
                        
                    send_email_attachment(results('authentication', 6), 
                                          results('authentication', 8), 
                                          results('authentication', 9), 
                                          results('authentication', 7),
                                    'attachment', result)
                    logging.info(
                        f"E-MAIL RESULT '{search}' SEND CORRECT")
                    
            elif hash_db(lines[3]) == results('hash', 2)  and download in file:
                with open(orders, 'r+', encoding="UTF-8") as file_object:
                    file = file_object.read()
                    lines = file.split('\n')

                    send_email_attachment(results('authentication', 6), 
                                          results('authentication', 8), 
                                          results('authentication', 9), 
                                          results('authentication', 7), 
                                        'attachment', 
                                        f'{folder_scan}\\{lines[5]}')
                    logging.info(
                        f"E-MAIL ATTACHMENT '{lines[5]}' SEND CORRECT")
                    
    except Exception as error:
        logging.warning(f"{type(error).__name__} {error} at file {__file__}")
