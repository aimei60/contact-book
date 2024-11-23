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

user = input("Enter the action for the contact book: ADD CONTACT, VIEW CONTACT, UPDATE CONTACT, DELETE CONTACT: ")

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    email_address = input("Enter Email Address: ")
    
    cur.execute('INSERT INTO contactbook (Name, Phone_Number, Address, Email_Address) VALUES (?, ?, ?, ?)', (name, phone, address, email_address))
    
    connection.commit()
    print("Contact added successfully!")
    

def view_contact():
    pass

def delete_contact():
    pass

def update_contact():
    pass

connection.close()