'''
There are quite a few ways to attach files to an email, but this is one of the simpler ways. This time we will use an encoder and MIMEMultipart from the email module and os.path to simply get the filename from the provided path.
This method supports text files, images, videos, audio and pdfs.
Once again, replacing the previous variables but setting the new variable 'file_location' to the location of the tile that you want to send, the email will now send with the file attached.

'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

email = 'ankanmazumdar2016@gmail.com' # Your email
password = '8910651838' # Your email account password
send_to_email = 'ankanmazumdar2016@gmail.com' # Who you are sending the message to
message = 'This is my attachment message' # The message in the email
subject = 'This is the attchment wala subject' # The subject line
file_location = 'C:\\Users\Ankan\Pictures\mauza info.docx'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

# Setup the attachment
filename = os.path.basename(file_location)
attachment = open(file_location, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# Attach the attachment to the MIMEMultipart object
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()