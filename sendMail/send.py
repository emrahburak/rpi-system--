#!/usr/bin/python3

import os
import smtplib  
import uuid
# from dotenv import dotenv_values
from email.message import EmailMessage

# config = dotenv_values(".env")
email = os.environ["EMAIL"]
passwd = os.environ["PASSWORD"]

# def get_cpu():
#     cmd = "sudo cpu | grep  'Arch\\|Temp\\|Gover\\|CPU'"
#     return os.system(cmd)

if email and passwd:
    sender_add = email  # storing the sender's mail id
    receiver_add = email  # storing the receiver's mail id
    password = passwd  # storing the password to log in
    # creating the SMTP server object by giving SMPT server address and port number

    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.ehlo()  # setting the ESMTP protocol
    smtp_server.starttls()  # setting up to TLS connection
    smtp_server.ehlo()  # calling the ehlo() again as encryption happens on calling startttls()
    smtp_server.login(sender_add, password)  # logging into out email id


    msg = EmailMessage()
    session_id = uuid.uuid4().hex

    msg_to_be_sent = '''
    Test ! session: {}
    Hello, Human!
    Hope you are doing well.
    System ready
    '''.format(session_id)

    msg.set_content(msg_to_be_sent)
    msg['Subject'] = "Hello from dietpi/ebg sessionID: {}".format(session_id)
    msg['From'] = sender_add
    msg['To'] = receiver_add
    # sending the mail by specifying the from and to address and the message
    # smtp_server.sendmail(sender_add, receiver_add, msg_to_be_sent)
    smtp_server.send_message(msg)
    # priting a message on sending the mail
    print('Successfully the mail is sent at session: {}'.format(session_id))
    smtp_server.quit()  # terminating the server
else:
    print("Error: Please create .env file")
