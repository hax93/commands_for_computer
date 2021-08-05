import time
import os
from email_move_task import imap_login
from tasks_for_computer import count_word


filename = 'task/tasks.txt'
powershell_result = 'C:\log_powershell.txt' #   my directory log txt file

while True:
    time.sleep(0)
    imap_login('xyz@xyz.com', 'password', 'imap', 'watch_email')
    count_word(filename)
    time.sleep(4)
    open(filename, 'w').close() #   clear txt file
    open(powershell_result, 'w').close() #  clear result powershell
    #   actually kill all process powershell.exe,
    #   will change in future
    os.system('wmic process where name="powershell.exe" delete')

