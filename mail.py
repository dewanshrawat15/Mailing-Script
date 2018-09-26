import smtplib
import csv
import re
 
username = ""
password = ""
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)

with open('db.csv') as data:
	row = csv.DictReader(data)
	for line in row:
		name = line['fullname']
		msg = "Hey"+name+" ! Hope you're having a good time!"
		add = line['email']
		server.sendmail("dewanshrawat15@gmail.com", add, msg)

server.quit()
