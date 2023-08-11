'''
nmap Scanner Program

StudentID: P2227171
Name: Swaathi Lakshmanan
Class: DISM/FT/1B/05
Assessment: CA1-2

Script name:
nmap-scanner.py

Purpose: 
This is the program does an nmap scan.

Usage Syntax:
Run with command line: python .\main.py

Python version:
Python 3

Reference:
None

Library/Module:
Install nmap package - pip install nmap

Known issues:
None
'''
# Imports
import nmap
from tabulate import tabulate

def printNmap():
    # Function for scanning nmap ports and outputting a table
    nmScan = nmap.PortScanner()
    print(f'Type of nmScan : {type(nmScan)}')
    IP = 'localhost scanme.nmap.org'
    print(f'Scanning ports: {IP}')
    results = nmScan.scan(hosts=IP, arguments='-v -sV --top-ports 10 -sTU -sC -O --traceroute')
    print(f'Type of results: {type(results)}')
    emptylist=[]
    protosToScan=['tcp','udp']
    infolist=['state','product','extrainfo','reason','cpe']
    for host in results['scan']:
        for proto in protosToScan:
            subdic2=results['scan'][host][proto]
            for port in subdic2:
                sublist1=[]
                sublist1.append(host)
                subdic1=results['scan'][host]['hostnames'][0]
                sublist1.append(subdic1['name'])
                sublist1.append(proto)
                sublist1.append(port)
                for i in infolist:
                    sublist1.append(subdic2[port][i])
                emptylist.append(sublist1)
    print(tabulate(emptylist, headers=['Host','Hostname','Protocol','port ID','State','Product','Extrainfo','Reason','CPE'],tablefmt="fancy_grid"))