'''
ftp Server Program

StudentID: P2227171
Name: Swaathi Lakshmanan
Class: DISM/FT/1B/05
Assessment: CA1-2

Script name:
ftp-server.py

Purpose: 
This is the program for the ftp server.

Usage Syntax:
Run with command line: python .\main.py

Input/output folders:
d:/psec_ca2/ftpClientData
d:/psec_ca2/ftpServerData

Python version:
Python 3

Reference:
https://regexlib.com/Search.aspx?k=file+path&AspxAutoDetectCookieSupport=1

Library/Module:
Install pyftpdlib module - pip install pyftpdlib

Known issues:
None
'''
# Imports
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import sys

class CustomHandler(FTPHandler):
    def on_disconnect(self):
        super().on_disconnect()
        sys.exit(0)


#  Block of code to start FTP server
authorizer = DummyAuthorizer()
serverdir='./ftpServerData/'
authorizer.add_anonymous(serverdir, perm='elrw')
handler = CustomHandler
handler.authorizer = authorizer
address = ('127.0.0.1', 2121)
server = FTPServer(address, handler)
server.serve_forever()