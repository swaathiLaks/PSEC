'''
ftp Client Program

StudentID: P2227171
Name: Swaathi Lakshmanan
Class: DISM/FT/1B/05
Assessment: CA1-2

Script name:
ftp-client.py

Purpose: 
This is the program is for the ftp client.

Usage Syntax:
Run with command line: python .\main.py

Input/output folders:
d:/psec_ca2/ftpClientData
d:/psec_ca2/ftpServerData

Python version:
Python 3

Reference:
https://pythonspot.com/ftp-client-in-python/

Library/Module:
Install pyftpdlib module - pip install pyftpdlib

Known issues:
None
'''
# Imports
import ftplib, os
ftp = ftplib.FTP()

def to_connect():
  # Function to connect to server
  ftp.connect('127.0.0.1', 2121)
  ftp.login()

def getFile(ftp, filename):
  # Function to download a file to ftpClientData. ftp refers to ftp and filename refers to the file the user intends to download.
  try:
    ftp.retrbinary("RETR " + filename ,open('./ftpClientData/'+filename, 'wb').write)
    return True
  except:
    return False

def upload(ftp, file):
  # Function to upload a file to ftpServerData. ftp refers to ftp and file refers to the file the user intends to download
  try:
    with open(os.path.join('ftpClientData',file),'rb') as file2:
      ftp.storbinary(f'STOR {file}',file2)
    file2.close()
    return True
  except:
    return False

def chooseFile(ftp, homedir=False):
  # Choose file lists the files already available in the folder which you are uploading or downloading from. ftp refers to ftp and homedir refers to whether the user intends to upload.
  data,moddata = [],[]
  if homedir:
    data=os.listdir(ftp)
  else:
    ftp.dir(data.append)
  for strx in data:
    subdat= strx.split(' ')
    moddata.append(subdat[-1])
  for num,stry in list(enumerate(data,1)):
    print(f'{num})\t{stry}')
  boolz=True
  download="download"
  if homedir:
    download="upload"
  while boolz:
    try:
      usernum=int(input(f'Enter the num of the file to {download}? '))
      if usernum<1 or usernum>len(data):
        raise Exception
      boolz=False
      usernum-=1
    except:
      print("Please enter a valid integer within given range.")
  return moddata[usernum]

file_download=""

def upordownload():
  # This is the main menu loop for uploading or downloading from the ftp server.
  menutxt="Would you like to \n1) upload\n2) download\n>>"
  bool1=True
  while bool1:
    y=True
    try:
      usernum=int(input(menutxt))
      if usernum==1:
        file1=chooseFile("./ftpClientData", True)
        to_connect()
        y=upload(ftp,file1)
        print(f'Uploading {file1}')
        ftp.quit()
        bool1=False
      elif usernum==2:
        to_connect()
        file2=chooseFile(ftp)
        y=getFile(ftp,file2)
        print(f'Downloading {file2}')
        ftp.quit()
        bool1=False
      else:
        raise Exception
    except:
      if y:
        print("Please enter a valid input.")
      else:
        if usernum==1:
          print(f"There was an error uploading {file1}.")
        if usernum==2:
          print(f"There was an error downloading {file2}.")