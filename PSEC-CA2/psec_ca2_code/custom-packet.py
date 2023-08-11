'''
Custom Packet Program

StudentID: P2227171
Name: Swaathi Lakshmanan
Class: DISM/FT/1B/05
Assessment: CA1-2

Script name:
custom-packet.py

Purpose: 
This is the program sends custom messages.

Usage Syntax:
Run with command line: python .\main.py

Python version:
Python 3

Reference:
None

Library/Module:
Install scapy package - pip install scapy
Install socket package - pip install socket
Install regex package - pip install regex

Known issues:
None
'''
from scapy.all import send, IP, TCP, ICMP, UDP, sr, sr1
import socket, re
# function check if website exists

def webexists(whichinp):
  # Function to check if the host name entered is valid and exists
  repat1=re.compile("/[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)?/gi")
  x=True
  while x:
    try:
      srcadd= input(f"Enter {whichinp} address of packet: ")
      repat1.match(srcadd)
      if socket.gethostbyname(srcadd):
        x=False
      return srcadd
    except:
      print("Invalid host")

def portopen(whichport,thestr):
  # Function to check if the port entered is valid
  x=True
  while x:
    try:
      port=int(input(whichport))
      if port<0 or port>65535:
        raise Exception
      x= False
      return port   
    except:
      print(f"{thestr} is invalid.")
def whichp():
  x = True
  while x:
    try:
      pkt_type = input("Enter Type (T) TCP, (U) UDP, (I) ICMP echo request (T/U/I): ").upper()
      if pkt_type!='U' and pkt_type!='T'and pkt_type!='I':
        raise Exception
      x = False
      return pkt_type
    except:
      print("enter a valid protocol")

def send_packet(src_addr:str , src_port:int , dest_addr:str, 
                 dest_port:int, pkt_type:str, pkt_data:str)  -> bool:
                #  Function from sample with previously written functions incorperated into it. Function for main input loop to generate custom packets.
  """Create and send a packet based on the provided parameters

  Args:
      src_addr(str) : Source IP address
      src_port(int) : Source Port
      dest_addr(str): Destination IP address
      dest_port(int): Destination Port
      pkt_type(str) : Type of packet (T)TCP, (U)UDP, (I)ICMP echo request. Note it is case sensitive
      pkt_data(str) : Data in the packet
  Returns:
      bool: True if send successfull, False otherwise
  """    

  if pkt_type == "T":
      pkt = IP(dst=dest_addr,src=src_addr)/TCP(dport=dest_port,sport=src_port)/pkt_data
  elif  pkt_type == "U":
      pkt = IP(dst=dest_addr,src=src_addr)/UDP(dport=dest_port,sport=src_port)/pkt_data
  elif pkt_type=="I":
      pkt = IP(dst=dest_addr,src=src_addr)/ICMP()/pkt_data
  try:
    send(pkt ,verbose = False)   # Hide "Send 1 packets" message on console
    return True
  except:
    return False

def print_custom_menu():
  """Obtain inputs to create custom packet

  Returns: Nil
  """    
  print("************************")
  print("*     Custom Packet    *")
  print("************************\n")
  src_addr = webexists("source")
  src_port = portopen("Enter source port of packet: ","Port") 
  dest_addr= webexists("destination")
  dest_port= portopen("Enter destination port of packet: ","Port")
  pkt_type = whichp()
        
  pkt_data = input("Packet RAW Data (optional, DISM-DISM-DISM-DISM left blank): ")
  if pkt_data == "":
    pkt_data = "DISM-DISM-DISM-DISM"
    
  pkt_count = portopen("No of Packet to send (1-65535): ","Number")
  start_now = input("Enter Y to Start, Any other return to main menu: ")

  if start_now.lower() != "y": 
    return
  else:
    count = 0
    for i in range(pkt_count):
      if send_packet(src_addr, src_port, dest_addr, dest_port, pkt_type, pkt_data):
        count  = count + 1

    print(count , " packet(s) sent" )

