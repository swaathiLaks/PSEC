'''
Main Program

StudentID: P2227171
Name: Swaathi Lakshmanan
Class: DISM/FT/1B/05
Assessment: CA1-2

Script name:
main.py

Purpose: 
This is the main program that imports all files and contains the loop for the main menu.

Usage Syntax:
Run with command line: python .\main.py

Python version:
Python 3

Reference:
None

Library/Module:
Install importlib package - pip install importlib
Install pyftpdlib module - pip install pyftpdlib

Known issues:
None
'''
# Imports
import importlib
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import subprocess
import os
nmapscanner = importlib.import_module('nmap-scanner')
customPacket=importlib.import_module('custom-packet')
mainMenutxt="** PSEC Info Security Apps **\n1) Scan network\n2) Upload/download file using FTP\n3) Send custom packet\n4) Quit\n\nYour input: "

def mainMenu():
    # Function for the main menu loop.
    x=True
    while x:
        try:
            userval=int(input(mainMenutxt))
            if userval==1:
                nmapscanner.printNmap()
            elif userval==2: 
                subprocess.Popen(f'start python ftp-server.py', shell=True)
                ftpClient= importlib.import_module('ftp-client')
                ftpClient.upordownload()
            elif userval==3:
                customPacket.print_custom_menu()
            elif userval==4:
                print('Goodbye.')
                x=False
            else:
                raise Exception
        except:
            print("Inavlid input. Enter an integer within given range.")
mainMenu()