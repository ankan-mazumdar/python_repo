import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Multipurpose Internet Mail Extensions (MIME) is an Internet standard that extends the format of email messages to support text in character sets other than ASCII, as well as attachments of audio, video, images, and application programs.

email = 'ankanmazumdar2016@gmail.com' # Your email
password = '8910651838' # Your email account password
send_to_email = 'ankanmazumdar2016@gmail.com' # Who you are sending the message to
subject = 'This is the subject'
messageHTML = '<p>Visit <a href="https://nitratine.net/">nitratine.net<a> for some great <span style="color: #496dd0">tutorials and projects!</span><p>'
messagePlain = 'Visit nitratine.net for some great tutorials and projects!'

msg = MIMEMultipart('alternative')
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

# Attach both plain and HTML versions
msg.attach(MIMEText(messagePlain, 'plain'))
msg.attach(MIMEText(messageHTML, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()