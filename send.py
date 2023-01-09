#!/usr/bin/python3.9

import smtplib  # importing the module
from dotenv import dotenv_values
from email.message import EmailMessage

config = dotenv_values(".env")

if config:
    if config["EMAIL"] and config["PASSWORD"]:
        sender_add = config["EMAIL"]  # storing the sender's mail id
        receiver_add = config["EMAIL"]  # storing the receiver's mail id
        password = config["PASSWORD"]  # storing the password to log in
        # creating the SMTP server object by giving SMPT server address and port number

        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.ehlo()  # setting the ESMTP protocol
        smtp_server.starttls()  # setting up to TLS connection
        smtp_server.ehlo()  # calling the ehlo() again as encryption happens on calling startttls()
        smtp_server.login(sender_add, password)  # logging into out email id

        msg = EmailMessage()


        msg_to_be_sent = '''
        Test !
        Hello, Human!
        Hope you are doing well.
        System ready
        '''
        msg.set_content(msg_to_be_sent)
        msg['Subject'] = "Hello from dietpi/ebg"
        msg['From'] = sender_add
        msg['To'] = receiver_add
        # sending the mail by specifying the from and to address and the message
        # smtp_server.sendmail(sender_add, receiver_add, msg_to_be_sent)
        smtp_server.send_message(msg)
        # priting a message on sending the mail
        print('Successfully the mail is sent')
        smtp_server.quit()  # terminating the server
    else:
        print("Please fill the blanks in .env file")

else:
    print("Error: Please create .env file")
