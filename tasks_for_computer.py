import os
import glob
import getpass
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

orders = f'c:\\Users\\{user}\\Documents\\backup\\inbox.txt'
result = f'c:\\Users\\{user}\\Documents\\backup\\results.txt'
folder_scan = f'c:\\Users\\{user}\\Documents'

def check_words(filename, file_extension, folder_scan):
    try:
        # if you want more EXTENSION just add below e.g. ,xml
        EXTENSION = "*,txt,docx,doc,xlsx,pdf"
        data = []
        show = 'show'        
        download = 'download'

        with open(filename, 'r+', encoding="UTF-8") as file_object:
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
           
                    with open(file_extension, 'w', encoding='utf-8') as files:
                        files.write(my_string)
                        
                    send_email_attachment(results('authentication', 6), 
                                          results('authentication', 8), 
                                          results('authentication', 9), 
                                          results('authentication', 7),
                                    'attachment', result)
        
            elif hash_db(lines[3]) == results('hash', 2)  and download in file:
                with open(filename, 'r+', encoding="UTF-8") as file_object:
                    file = file_object.read()
                    lines = file.split('\n')

                    send_email_attachment(results('authentication', 6), 
                                          results('authentication', 8), 
                                          results('authentication', 9), 
                                          results('authentication', 7), 
                                        'attachment', 
                                        f'{folder_scan}\\{lines[5]}')
    except ValueError:
        pass
