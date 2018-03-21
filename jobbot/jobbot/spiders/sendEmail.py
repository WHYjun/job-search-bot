# -*- coding: utf-8 -*-
import os
import json

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts:
        for contact in contacts:
            names.append(contact.split()[0])
            emails.append(contact.split()[1])
    return names, emails

def writeMessage(name,companyName):
    message = "Hello " + name +",\n" \
            + "We found a new job posting at " + companyName + " on Job Bot.\n" \
            + "Thank you very much for using our services and we hope to provide you with more quality content in the future.\n\n" \
            + "Sincerely,\n" \
            + "The Job Bot Team"
    return message

def notify(company):
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'config.json')
    with open(filename) as f:
        datastore = json.load(f)
    f.close()

    ADDRESS = datastore['email']['address']
    PASSWORD = datastore['email']['pwd']
    HOST = datastore['server']['host']
    PORT = datastore['server']['port']
    names, emails = contacts(company+'.txt')

    s = smtplib.SMTP(HOST,int(PORT))
    s.starttls()
    s.login(ADDRESS, PASSWORD)

    for name, email in zip(names, emails):
        msg = MIMEMultipart()

        message = writeMessage(name, company)

        # print(message)
        filename = os.path.join(scriptpath, 'company.json')
        with open(filename) as f:
            companyName = json.load(f)
        f.close()

        msg['From']=ADDRESS
        msg['To']=email
        msg['Subject']="Found a new job posting at " + companyName[company]

        msg.attach(MIMEText(message, 'plain'))

        s.send_message(msg)
        del msg
        
    s.quit()