import sfpm

target = 'target email'
subject = 'subject'

# Either write a message or write a text file path
message = 'your message/file path'

# Do not declare to use standard password
login = 'your email'
password = 'your password'

sfpm.sendEmail(target, subject, message, login, password)
# You can use:
# sfpm.sendEmail(target, subject, message)
# if standard email is set
