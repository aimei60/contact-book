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

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    email_address = input("Enter Email Address: ")
    
    
    cur.execute('INSERT INTO contactbook (Name, Phone_Number, Address, Email_Address) VALUES (?, ?, ?, ?)',
                    (name, phone, address, email_address))
        
    connection.commit()
    print("Contact added successfully!")

def view_contact():
    cur.execute('SELECT Name FROM contactbook')
    
    rows = cur.fetchall()
    for row in rows:
        for i in row:
         print(i)
        
    view_contact = input("Which contact's details would you like to view? Enter the name: ").strip()
    
    cur.execute('SELECT * FROM contactbook WHERE LOWER(Name) = LOWER(?)', (view_contact,))
    contact_details = cur.fetchone()
    
    if contact_details:
        for i in contact_details:
            print(i)
    else:
        print("No contact found in that name.")
        
def delete_contact():
    cur.execute('SELECT Name FROM contactbook')
        
    rows = cur.fetchall()
    for row in rows:
        for i in row:
            print(i)
            
    delete_contact = input("Which contact's details would you like to delete? Enter the name: ").strip()
        
    cur.execute('SELECT Name FROM contactbook WHERE LOWER(Name) = LOWER(?)', (delete_contact,))
    record = cur.fetchone()
        
    if record:
        cur.execute('DELETE FROM contactbook WHERE LOWER(Name) = LOWER(?)', (delete_contact,))
        connection.commit()
        print(f"Contact '{record[0]}' successfully deleted!")
    else:
        print("Contact not in contact book")
        
def update_contact():
    cur.execute('SELECT Name FROM contactbook')
    
    rows = cur.fetchall()
    for row in rows:
        for i in row:
         print(i)
        
    view_contact = input("Which contact's details would you like to update? Enter the name: ").strip().lower()
    
    cur.execute('SELECT * FROM contactbook WHERE LOWER(Name) = LOWER(?)', (view_contact,))
    contact_details = cur.fetchone()
    
    if contact_details:
        for i in contact_details:
            print(i)
    else:
        print("No contact found in that name.")
    
    updateContact = input("Which details would you like to update? ").strip().lower()
    
    if updateContact == "name":
        name = input("State the name to update: ").strip().lower()
        cur.execute('UPDATE contactbook SET Name = ? WHERE LOWER(Name) = LOWER(?)', (name, view_contact,))
        connection.commit()
        print(f"Updated Name to {name}!")
    elif updateContact == "phone number":
        phone_num = input("State the phone number to update: ").strip().lower()
        cur.execute('UPDATE contactbook SET Phone_Number = ? WHERE LOWER(Name) = LOWER(?)', (phone_num, view_contact,))
        connection.commit()
        print(f"Updated Phone Number to {phone_num}")
    elif updateContact == "address":
        address = input("State the new address to update: ").strip().lower()
        cur.execute('UPDATE contactbook SET Address = ? WHERE LOWER(Name) = LOWER(?)', (address, view_contact,))
        connection.commit()
        print(f"Updated Address to {address}")
    elif updateContact == "email address":
        email_add = input("State the new email address to update: ").strip().lower()
        cur.execute('UPDATE contactbook SET Email_Address = ? WHERE LOWER(Name) = LOWER(?)', (email_add, view_contact,))
        connection.commit()
        print(f"Email Address updated to {email_add}")
    else:
        print("Not a valid response. Please choose from Name, Phone Number, Address or Email Address")
    
def contactbook():
    user = input("Enter the action for the contact book: ADD CONTACT, VIEW CONTACT, UPDATE CONTACT, DELETE CONTACT: ").strip().lower()
    
    if user == "add contact":
        add_contact()
    elif user == "view contact":
        view_contact()
    elif user == "delete contact":
        delete_contact()
    elif user == "update contact":
        update_contact()

if __name__ == "__main__":
    contactbook()

connection.close()
