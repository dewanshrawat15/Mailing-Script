SMTPserver = ''
sender = ''

USERNAME = ""
PASSWORD = ""


subject=""                                  

import sys
import os
import re
import csv
import time

from smtplib import SMTP_SSL as SMTP        

from email.mime.text import MIMEText

conn = SMTP(SMTPserver)
conn.set_debuglevel(False)
conn.login(USERNAME, PASSWORD)
with open('tbm.csv') as data:
    row = csv.DictReader(data)
    for line in row:
        name = line['First Name']
        add = line['Email']
        text_subtype = 'html'               
        
        content="""\

        """                                 
        msg = MIMEText(content, text_subtype)
        try:
            msg['Subject'] = subject
            msg['From'] = sender 
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
