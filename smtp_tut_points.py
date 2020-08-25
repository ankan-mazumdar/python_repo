#!/usr/bin/python

import smtplib

sender = 'ankanmazumdar2016@gmail.com'
receivers = ['ankanmazumdar2016@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
    smtpObj.ehlo()
    '''Identify yourself to an ESMTP server using EHLO,
    it should not be necessary to call this method explicitly. It will be implicitly called by sendmail() when necessary., 
    exception smtplib.SMTPHeloError
    The server refused our HELO message.
    '''
    smtpObj.starttls()
    #SMTP.starttls(keyfile=None, certfile=None, context=None)
    #Put the SMTP connection in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted. You should then call ehlo() again.
    smtpObj.ehlo()
    smtpObj.login("ankanmazumdar2016@gmail.com","8910651838")
    smtpObj.sendmail(sender, receivers, message)         
    print("Successfully sent email")
except SMTPException:
    print("Error: unable to send email")



'''
def send_email():
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('My Gmail ID', 'My password')
message = 'sending this from python!'
server.sendmail('My Gmail ID', 'Recipient's mail Id ', message)
'''
smtpObj.quit()
