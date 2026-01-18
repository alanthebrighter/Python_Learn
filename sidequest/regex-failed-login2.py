#! /bin/python3

import re

def failedAttempts(log):
    patern = r'(\d{2}:\d{2}:\d{2}).*?Failed password.*?from\s+((?:\d{1,3}\.){3}\d{1,3})'
    return re.findall(patern, log)


log = """
Jan 18 12:05:01 server sshd[1234]: Accepted password for admin from 10.0.0.5 port 22
Jan 18 12:06:15 server sshd[1235]: Failed password for invalid user guest from 192.168.1.105 port 22
Jan 18 12:06:20 server sshd[1236]: Failed password for root from 172.16.0.20 port 22
Jan 18 12:07:00 server sshd[1237]: Connection closed by 10.0.0.5
Jan 18 12:08:12 server sshd[1238]: Failed password for admin from 192.168.1.105 port 22
"""

print(failedAttempts(log))
