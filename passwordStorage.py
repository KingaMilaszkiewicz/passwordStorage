import sqlite3
import base64
import os
import PyQt5

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

conn = sqlite3.connect("passwords.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS passwords (host TEXT, username TEXT, email TEXT, password TEXT, UNIQUE (host, username, email, password))")

# encoding a password
password_provided = input("Password: ")
password = password_provided.encode()
salt = b'fEkB?XKedEUuyk7r'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key=base64.urlsafe_b64encode(kdf.derive(password))

def searchdata():
    hostsearch = input("Please enter the host name: ")
    # make a list and fill it with all the rows of the result of the query, because of the way SQL works,
    # we can't know how big the result is without running a separate query that returns a COUNT()
    result = [row for row in c.execute(f"SELECT * FROM passwords WHERE host = '{hostsearch}'")]
    if len(result) > 0:
        for row in result:
            print("Host:", row[0], "\nUsername:", row[1], "\nEmail:", row[2], "\nPassword:", row[3])
    else:
        print("No such hostname!")

def adddata():
    hostname = input("Enter host name:")
    username = input("Enter user name:")
    email = input("Enter email:")
    password = input("Enter password:")
    c.execute(f"INSERT OR IGNORE INTO passwords VALUES ('{hostname}','{username}','{email}','{password}')")
    conn.commit()
    print("You've successfully submitted data for", hostname, "!")

def editdata():
    hostsearch = input("Please enter host name: ")

    hostname = input("Enter host name:")
    username = input("Enter user name:")
    email = input("Enter email:")
    password = input("Enter password:")
    c.execute(f"UPDATE passwords SET host = '{hostname}', username = '{username}', email = '{email}', password = '{password}' WHERE host = '{hostsearch}'")
    conn.commit()
    print("You've updated", hostname, "successfully!")

def deletedata():
    hostsearch = input("Please enter host name: ")
    c.execute(f"DELETE FROM passwords WHERE host ='{hostsearch}'")
    conn.commit()
    print("You've deleted", hostsearch, "successfully!")

def showalldata():
    for row in c.execute(f"SELECT * FROM passwords"):
        print(row)

while True:
    try:
        userinput = int(input("""Do you want to:
        1. Search data
        2. Add data
        3. Edit data
        4. Delete data
        5. Show all data
        6. Exit
        Input a number: """))

        if userinput == 1:
            searchdata()
        elif userinput == 2:
            adddata()
        elif userinput == 3:
            editdata()
        elif userinput == 4:
            deletedata()
        elif userinput == 5:
            showalldata()
        elif userinput == 6:
            print("Goodbye!")
            break
        else:
            print("Please enter a number from 1 to 5")
    except ValueError:
        print("Please enter a number from 1 to 5")

conn.close()
