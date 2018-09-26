SMTPserver = 'mail.edcbvucoep.com'
sender = 'contact@edcbvucoep.com'

USERNAME = "edcbvucoep"
PASSWORD = "Edcbvucoe@1234"

# typical values for text_subtype are plain, html, xml

subject="Invite for Startup Conclave 2.0 : EDC BVUCOEP"

import sys
import os
import re
import csv
import time

from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

# old version
# from email.MIMEText import MIMEText
from email.mime.text import MIMEText

with open('db.csv') as data:
    row = csv.DictReader(data)
    for line in row:
        conn = SMTP(SMTPserver)
        conn.set_debuglevel(False)
        conn.login(USERNAME, PASSWORD)
        name = line['fullname']
        add = line['email']
        text_subtype = 'html'        
        content="""\

            <center><img src="https://www.edcbvucoep.com/masthead.jpg" width="631" height="273"></center>
            <br><br>
            Dear """+name+""",<br><br>
            We, the <a href="https://www.edcbvucoep.com/">Entrepreneurship Development Cell of Bharati Vidyapeeth College of Engineering, Pune</a> is glad to invite you to it’s one of the main event, Startup Conclave 2.0 on  5th and 6th of October 2018.<br><br>
            The event will guide the participants through the journey of entrepreneurship, the importance of team-building and also host workshops on Technical and Business tracks, exciting competitions to gain a deeper understanding of these kinds of stuff.<br><br>
            On <u><strong>Day 1</strong></u> we have: <br>
            <ol>
            <li>Panel Discussion with the theme “INNOVATION and IMPACT”.
            <li>Technical and Business Tracks workshop.
            </ol><br>
            <strong><u>The Technical track</u></strong> would include :<br><br>
            A one-hour tech-seminar on the topic of Blockchain and its applications.<br>
            A hands-on workshop of 2 hours on BIG-DATA.<br><br>
            <strong><u>The Business track</u></strong> would include:<br>
            A one-hour business-seminar on the topic  Strategy planning in the corporate world.<br>
            A hands-on workshop of 2 hours on Creativity in Digital Marketing.<br><br>
            <strong><u>On Day 2 :</u></strong><br><br>
            The event would host the Code Relay, a very interesting competition for coders and Estrategia, a competition which would be teaching students about building strategies in the corporate ecosystem.<br><br>
            In this event, we not only have people coming from startup culture but also from technological and business background as well. This brings a lot of opportunities to build in networks and learn about around the world. Also, it has students and experts coming from different fields which further would help you know more about the latest requirements and interests of them.<br><br>
            <bold>Venue:</bold> Bharati Vidyapeeth College of Engineering.<br>
            <bold>Date:</bold> 5th and 6th of October 2018.
            <br><br>
            The event details are hereby attached. <a href="https://www.edcbvucoep.com/conclave/Proposal.pdf">Details</a><br>
            We would be glad if you will be a part of the event. Click here to <a href="https://conclave.edcbvucoep.com/">Register</a><br><br>
            Regards<br>
            Team EDC<br>
            BVUCOEP<br><br>
            Facebook: <a href="http://www.fb.com/edcbvucoep">Facebook</a><br>
            Twitter: <a href="http://www.twitter.com/edcbvucoep">Twitter</a><br>
            Instagram: <a href="http://www.instagram.com/edcbvucoe">Instagram</a><br>
            Snapchat: @edcbvucoep<br>
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
        finally:
            conn.quit()

conn.quit()
# except:
#     sys.exit( "mail failed; %s" % "CUSTOM_ERROR" ) # give an error message