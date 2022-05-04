import time
import getpass
import traceback
from email_move_task import email_task
from tasks_for_computer import check_words
from create_files import *
from settings_db import *

user = getpass.getuser()

orders = f'c:\\Users\\{user}\\Documents\\backup\\inbox.txt'
result = f'c:\\Users\\{user}\\Documents\\backup\\results.txt'
folder_scan = f'c:\\Users\\{user}\\Documents'

def data_email():
    add_table_email('authentication')
    login = input("E-MAIL: ")
    login_password = input("PASSWORD: ")
    imap = input("IMAP E-MAIL: ")
    from_email = input("FOLLOW E-MAIL: ")
    sender_email = input("E-MAIL SEND ATTACHMENT: ")
    smtp = input("SMTP E-MAIL: ")
    sender_password = input("SENDER E-MAIL PASSWORD: ")
    send_to = input("E-MAIL RECIPIENT: ")
    add_data_email('authentication', imap, login, login_password, from_email, 
                   sender_email, send_to, smtp, sender_password)
    
def add_password_program():
    passw = input("PASSWORD FOR PROGRAM/COMMUNICATE COMPUTER:\n>>>")
    add_password_table('hash')
    hash_db(passw)
    add_password('hash')
    print("PASSWORD ADDED")

def start_program():
    check = getpass.getpass('Typing Password:\n>>>>>')

    if hash_db(check) == results('hash', 2):
        print("Correct!")
        while True:
            time.sleep(900)
            email_task(orders, results('authentication', 3), 
                       results('authentication', 4),
                       results('authentication', 2), 
                       results('authentication', 5), typ='')
            check_words(orders, result, folder_scan)
            #   clear txt
            open(orders, 'w').close()
            open(result, 'w').close()

    else:
        print("Password Wrong :<")
    
def change_passw():
    try:
        del_table('hash')
        print("Password Delete")
    except:
        print("Data not available, create password.")

def del_db():
    try:
        del_db_file()
    except FileNotFoundError:
        traceback.print_exc()
        print()

if __name__ =='__main__':
    
    txt = ['inbox', 'results']
    create_folder()
    for i in txt:
        create_files(i)

    while True:
        print("0. ADD Data email.")
        print("1. ADD password.")
        print("2. START program.")
        print("3. CHANGE password.")
        print("4. Delete ALL data.")
        decision = input("5. EXIT program.\n-")
        
        match decision:
            case '0':
                data_email()
                print()
            case '1':
                add_password_program()
            case '2':
                start_program()
            case '3':
                change_passw()            
            case '4':
                del_db()
            case '5':
                print("SEE YOU NEXT TIME!\n")
                break
            case _:
                print("Typing number!\n")
