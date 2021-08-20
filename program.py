import time
from email_move_task import imap_login
from tasks_for_computer import count_word


filename = 'task/tasks.txt'
file_extension = 'task/file_extension.txt'  
while True:
    time.sleep(0)                         
    imap_login('xyz@xyz.com', 'password', 'imap', 'watch_email')
    count_word(filename)
    time.sleep(4)
    open(filename, 'w').close()           #  clear txt file
    open(file_extension, 'w').close()     #  clear result
