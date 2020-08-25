import smtplib

server= smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("ankanmazumdar2016@gmail.com","8910651838")
server.sendmail("ankanmazumdar2016@gmail.com","ankanmazumdar2016@gmail.com","sending my first mail using python")
#message='message send using message='
server.quit()