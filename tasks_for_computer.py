"""tasks for computer
1 - if we send subjet:secret and in text:*.xlsx
we get return email with attachment log all files
who have .xlsx.
2 - if we know what name file we got in computer,
we can send subject:download and text: budget.xlsx
then computer send email attachment with this file"""
#   remember get \\ for directory
import os, glob
from email_attachment import send_email_attachment

def count_word(filename, file_extension, folder_scan):
    try:
        data = []
        password = 'secret'        #we can change 'secret' or 'pobierz'
        download = 'pobierz'

        with open(filename, 'r+', encoding="UTF-8") as file_object:
            file = file_object.read()
            lines = file.split('\n')

            if password in file:

                command = lines[1]
                search = command   #command from email

                os.chdir(folder_scan)   #scan and try result output to file_extension.txt
                for direct in glob.glob(f'{search}'):
                    data.append(direct)

                my_string = ""

                for i in data:
                    my_string += ('{} \n').format(i)
                    
                with open(file_extension, 'w', encoding='utf-8') as files:
                    files.write(my_string)
                
                send_email_attachment('where send email@ with attachement',
                                 'attachment', 'file_extension.txt direct: send result scan')
        
            elif download in file:
                with open(filename, 'r+', encoding="UTF-8") as file_object:
                    file = file_object.read()
                    lines = file.split('\n')

                    send_email_attachment('where send email@ with attachement', 'attachment',
                                          f'folder with documents txt, xlsx, pdf etc{lines[1]}')
    except ValueError:
        pass
