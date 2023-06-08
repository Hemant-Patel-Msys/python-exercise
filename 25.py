# 25. Write a program to send a mail notification to customers regarding the arrival of goods
# on a daily basis. The admin email has a separate domain email address owned by your
# company.Do not forget to add cc candidates in customer’s mail.
import smtplib
#!/usr/bin/python
from smtplib import *


sender = 'hemantkurmi1998@gmail.com'
receivers = ['areakingpanna@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except:
   print("Error: unable to send email")