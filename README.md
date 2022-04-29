# sfpm

Simple library to send finished process messages

## Warning

Made this for my own use and only tested with gmail. No idea whether it works with different providers

## Structure

This library is a simple method for sending email messages in one line. It is intended to be used as a remote alert and automate messaging when running unattended python scripts.

## How to use

1 - Import the library

2 - Write messages in a text file or a string

3 - Call ***sfpm.sendEmail(target, subject, message, login, password)***

> or ***sfpm.sendEmail(target, subject, message)*** if standard login and password are set inside ***sfpm.py*** 

## Example

```python
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
```

## Setting standard credentials

Just change lines 7 and 8 in sfpm.py

```python
7 std_login = 'standard email'
8 std_password = 'standard email password'
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
