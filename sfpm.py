# Import the email modules we'll need
from email.message import EmailMessage
# Import smtplib for the actual sending function
import smtplib


std_login = 'standard email'
std_password = 'standard email password'


def sendEmail(target, subject, message, login=std_login, password=std_password):

    textfile = message
    # Open the plain text file whose name is in textfile for reading.
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = login
    msg['To'] = target
    try:
        with open(textfile) as fp:
            msg.set_content(fp.read())
    except:
        msg.set_content(message)

    # Send the message via gmail SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(login, password)
    server.send_message(msg)
    server.quit()

    print("e-mail sent to '", target, "'")
