"""tasks for computer
1 - if we send subjet:secret and in text:ls *.xlsx
we get return email with powershell log all files
who have .xlsx.
2 - if we know what name file we got in computer,
we can send subject:download and text: budget.xlsx
then computer send email attachment with this file"""
#   remember get \\ for directory
import time
import os
from powershell_automate import powershell_open, commands_with_log, back_directory
from email_attachment import send_email_attachment

def count_word(filename):
    try:
        password = 'secret'
        download = 'download'
        with open(filename, 'r+', encoding="UTF-8") as file_object:
            file = file_object.read()
            lines = file.split('\n')

            if password in file:
                powershell_open('here powershell directory')
                commands_with_log('folder with documents txt, xlsx, pdf etc', 'directory your log_powershell.txt', lines[1])
                send_email_attachment('where send email with attachement', 'attachment', 'directory your log_powershell.txt')
                time.sleep(4)
                back_directory('directory where u have all scripts this program')
                time.sleep(2)
        
            elif download in file:
                with open(filename, 'r+', encoding="UTF-8") as file_object:
                    file = file_object.read()
                    lines = file.split('\n')

                    send_email_attachment('where send email with attachement', 'attachment',
                                          f'folder with documents txt, xlsx, pdf etc{lines[1]}')
    except ValueError:
        pass
