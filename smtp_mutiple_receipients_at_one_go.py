import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Multipurpose Internet Mail Extensions (MIME) is an Internet standard that extends the format of email messages to support text in character sets other than ASCII, as well as attachments of audio, video, images, and application programs.

email = 'ankanmazumdar2016@gmail.com' # Your email
password = '8910651838' # Your email account password
send_to_emails = ['ankanmazumdar2016@gmail.com', 'rocksankan@gmail.com'] # Who you are sending the message to
message = 'This is email delievry to multiple receipients at one go' # The message in the email
subject = 'This is email delievry to multiple receipients at one go' # The subject line


msg = MIMEMultipart() #MIMEMultipartfunction invoked/called by masg object 
msg['From'] = email #arguments of multipart from, to & subject
# Was: msg['To'] = send_to_email
msg['To'] = ', '.join(send_to_emails)
msg['Subject'] = subject

 
msg.attach(MIMEText(message, 'plain'))  # Attach the message to the MIMEMultipart object

server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
server.starttls() # Use TLS
server.login(email, password) # Login to the email server
#text = msg.as_string() # now need to convert the attached MIMEMultipart object to a string to send
#server.sendmail(email, send_to_email, text)  # Send the email

# Was: server.sendmail(email, send_to_email, text) where text = msg.as_string()
server.send_message(msg) 
server.quit() # Logout of the email server