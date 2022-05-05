import time
import getpass
import traceback
import sys
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
    return "\n>PASSWORD ADDED\n"

def start_program():
    check = getpass.getpass('Typing Password:\n>>>>>')
    try:
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

    except Exception as error:
        print(f"create password: {type(error).__name__}".upper())
    
def change_passw():
    try:
        del_table('hash')
        return ">Password Delete"
    except:
        return "Data not available, create password."

def del_db():
    try:
        del_db_file()
    except FileNotFoundError:
        traceback.print_exc()
        print()
        
def exit_program():
    print("SEE YOU NEXT TIME!")
    return sys.exit()

def select():
    output = int(input('-'))
    return output

def main():
    txt = ['inbox', 'results']
    create_folder()
    for i in txt:
        create_files(i)

    while True:
        description = {}
        
        if bool(results('hash', 2)) is False:
            description[1] = ["ADD password.", add_password_program]
            
        if bool(results('authentication', 0)) is False:
            description[2] = ["ADD Data email.", data_email]
    
        if bool(results('authentication', 0)) and bool(results('hash', 0)) is True:
            description[3] = ["START program.", start_program]
            description[4] = ["CHANGE password.", change_passw]
        
        description[5] = ["DELETE all data.", del_db]
        description[6] = ["EXIT program.", exit_program]
            
        menu = {}  
        for n, v in enumerate(description.items()):
            print(f"{n}. {v[1][0]}")
            menu[n] = [v[1][0], v[1][1]] 

        def navigate(i):
            try:
                print(menu[i][1]()) 
            except Exception as error:
                print(f"ERROR: {type(error).__name__}\n"
                    f"typing number 0{1 - len(menu)}".upper())
                
        navigate(select())

if __name__ =='__main__':
    main()
