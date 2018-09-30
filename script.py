SMTPserver = ''
sender = ''

USERNAME = ""
PASSWORD = ""

# typical values for text_subtype are plain, html, xml

subject=""                                  # subject of the email

import sys
import os
import re
import csv
import time

from smtplib import SMTP_SSL as SMTP        # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

# old version
# from email.MIMEText import MIMEText
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
# except:
#     sys.exit( "mail failed; %s" % "CUSTOM_ERROR" ) # give an error message
