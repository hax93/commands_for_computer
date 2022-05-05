import hashlib
import sqlite3
import getpass
import os.path
import datetime

user = getpass.getuser()
filename = f'c:\\Users\\{user}\\Documents\\backup\\database.db'

class Database:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        # Close DB
        self.connection.close()

    def create_table(self, sql: str):
        self.cursor.execute(sql)
        self.connection.commit()

    def insert(self, table, *values):
        self.cursor.execute(
            f"INSERT INTO {table} VALUES ({','.join(['?' for _ in values])})", values)
        self.connection.commit()

    def fetch_all(self, table, **conditions):
        values = conditions.values()
        return self.cursor.execute(
            f"SELECT * FROM {table} WHERE ({' and '.join([f'{condition}=?' for condition in conditions])})",
            list(values)
        ) 

    def drop_table(self, table):
        self.cursor.execute(f"DROP TABLE {table}")
        self.connection.commit()

def del_table(table):
    db = Database(filename)
    db.drop_table(table)
    
def add_table_email(table):
    print("Create table in DB.") 
    db = Database(filename)
    db.create_table(f'''CREATE TABLE {table} 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT, 
                    imap TEXT, login TEXT, login_password TEXT, 
                    from_email TEXT, sender_email TEXT, send_to TEXT, 
                    smtp TEXT, sender_password TEXT)''')


def add_password_table(table):
    print("Create table in DB.") 
    db = Database(filename) 
    db.create_table(f'''CREATE TABLE {table} 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    data TEXT, password TEXT, date TEXT)''')

password = []
def add_password(table):
    # data, password, date
    print("Append new data to DB.")
    databa = 'data'
    date = str(datetime.datetime.now().date())
    db = Database(filename)
    db.insert(table, None, databa, password[0], date) 

def add_data_email(table, imap, login, login_password, 
                   from_email, sender_email, send_to, smtp, sender_password):
    print("Append new data to DB.")
    databa = 'data'

    db = Database(filename)
    db.insert(table, None, databa, imap, login, login_password, from_email, 
              sender_email, send_to, smtp, sender_password)          

def del_db_file():
    location = filename
    path = os.path.join(location)
    os.remove(path)
    print("Delete Database")
    
def results(table, n): 
    try:
        all = 'data'
        db = Database(filename)
        output = db.fetch_all(table, data=all)
    
        if table == 'hash':
            for i in output:
                return i[n]
        else:    
            for i in output:
                return i[n]   
    except:
        return False
        
def hash_db(string):
    # change hashlib if didn't working
    hash_func = hashlib.sha3_256()
    encoded_string = string.encode()
    hash_func.update(encoded_string)
    message = hash_func.hexdigest()
    password.append(message)
    return message
