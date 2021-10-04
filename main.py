import time
import getpass
from email_move_task import imap_login
from tasks_for_computer import count_word
from create_files import create_folder

try:
    create_folder('tasks.txt')
    create_folder('file_extension')
except FileExistsError:
    pass

user = (getpass.getuser())

filename = f'c:\\Users\\{user}\\Documents\\orders\\tasks.txt'
file_extension = f'c:\\Users\\{user}\\Documents\\orders\\file_extension.txt'
#where do you want to check/download files
folder_scan = f'c:\\Users\\{user}\\Documents'

while True:                        
    imap_login('xyz@xyz.com', 'password', 'imap', 'watch_email')
    count_word(filename, file_extension, folder_scan)
    time.sleep(4)
    open(filename, 'w').close()           #  clear txt file
    open(file_extension, 'w').close()     #  clear result
