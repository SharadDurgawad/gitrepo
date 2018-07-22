import smtplib

sender = 'durgawad@gmail.com'
passwd = input("Enter the password: ")

receiver = 'sharad.durgawad@gmail.com'
SUBJECT = 'SMTP TEST MAIL !!!'
TEXT = 'Hi There, This is a SMTP mail. \n\n Thanks & Regards, \n\n Sharad Durgawad'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(sender, passwd)

BODY = '\r\n'.join(['To: %s' % receiver,
                    'From: %s' % sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(sender, [receiver], BODY)
    print('Successfully sent the mail')
except smtplib.SMTPException:
    print("Error: unable to send email")

server.quit()
