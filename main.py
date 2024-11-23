"""
python and sqlite3
personal contact book
table with contact ID number, name, phone number, address, email
users can add new contacts
view all contacts
update contact details
delete a contact

user input and database interactions 

"""

import sqlite3

connection = sqlite3.connect("contactbook.db")

cur = connection.cursor()

"""cur.execute('''
    CREATE TABLE IF NOT EXISTS contactbook (
        ID_Number integer PRIMARY KEY AUTOINCREMENT,
        Name text, 
        Phone_Number text, 
        Address text, 
        Email_Address text)
    ''')
"""


connection.commit()
connection.close()