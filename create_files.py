import getpass
import os

user = (getpass.getuser())

def create_folder():
    try:
        os.mkdir(f'c:\\Users\\{user}\\Documents\\backup')
    except:
        pass
    
def create_files(name):
    filename = f'c:\\Users\\{user}\\Documents\\backup\\{name}.txt'
    
    if os.path.exists(filename) is True:
            True
    else:
        open(filename, 'w')
