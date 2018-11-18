import sys
from os import name, system
import re
import csv
import time
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
from getpass import getpass


def clear():
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
print("Ensure you have saved your database file in the .csv format in this very directory!")
time.sleep(5)

SMTPserver = input("Enter server address: ")
sender = input("Email through which mails are to be sent: ")
USERNAME = input("Enter cpanel username: ")
PASSWORD = getpass("Enter cpanel password: ")

db = input("Enter the database file name with the extension: ")
subject= input("Enter the subject of the email: ")

print("Establishing connection with server")
conn = SMTP(SMTPserver)
conn.set_debuglevel(False)
conn.login(USERNAME, PASSWORD)
print("Login Succesful!")
with open(''+db+'') as data:
    row = csv.DictReader(data)
    for line in row:
        name = line['First Name']
        add = line['Email']
        text_subtype = 'html'               
        # content
        content="""\
        """                                 
        msg = MIMEText(content, text_subtype)
        try:
            msg['Subject'] = subject
            msg['From'] = sender # some SMTP servers will do this automatically, not all
            # try:
            conn.sendmail(sender, add, msg.as_string())
            print('Mail sent to '+name+'')
        except:
            print('Output Sequence ended')
            time.sleep(2)
            print('SMTP secured')
            time.sleep(2)
            print('Terminating SMTP connection!')
            time.sleep(1)
            exit()

conn.quit()
