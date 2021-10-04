import getpass
import os

def create_folder(name):
    user = (getpass.getuser())
    filename = f'c:\\Users\\{user}\\Documents\\orders\\{name}'
    cwd = os.path.dirname(__file__) + f'\\{name}'
    try:
        os.mkdir(f'c:\\Users\\{user}\\Documents\\orders')
    except:
        pass
    
    try:
        open(filename, 'r')

    except FileNotFoundError:
        open(filename, 'w')
