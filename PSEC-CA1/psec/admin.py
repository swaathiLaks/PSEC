'''
Main Program

StudentID: P2227171
Name: Swaathi Lakshmanan
Class: DISM/FT/1B/05
Assessment: CA1-1

Script name:
admin.py

Purpose: 
Contains all the functions for the admin panel and the admin panel loop.

Usage Syntax:
(None)
Run with command line: python .\player.py

Input files:
d:/psec/game_log.txt
d:/psec/game_settings1.txt
d:/psec/hangman_hanged.txt
d:/psec/passwords.txt
d:/psec/word_list1.txt

Output files:
d:/psec/game_settings1.txt
d:/psec/hangman_hanged.txt
d:/psec/passwords.txt
d:/psec/word_list1.txt

Python version:
Python 3

Reference:
None

Library/Module:
None (to download)

Known issues:
None
'''

# imports
from datetime import datetime

# functions

# function to check if something is in the dictionary and reprompt
def checkifinDic(dic1,newinput):
    # dic1: dictionary to check for input in, newinput: the input itself
    for i in dic1:
        if i == newinput:
            return "exists"

# function to check if num or raise exception
def checkifInt(txt):
    # txt refers to the input to be check
    x=True
    while x:
        try:
            ifnum=int(input(txt))
            x=False
        except:
            print("Please enter a valid integer.\n")
    return ifnum

# function to check if num is within a specific range
def checkinRange(txt,rng):
    # txt refers to the input to check, rng refers to the range within which the input should be in
    x=True
    while x:
        try:
            ifnum=(input(txt))
            if ifnum=="":
                x=False
            elif not(int(ifnum)<(rng+2) and int(ifnum)>0):
                raise Exception
            x=False   
        except:
            print("Please enter an integer within the given range.\n")
    return ifnum

# function to check if input is a valid date
def checkList(y):
    # y refers to the input which should be checked for whether it is a valid date
    x=True
    while x:
        try:
            z=input(y).split('-')
            if not(int(z[0])<32 and int(z[0])>0) or not(int(z[1])<13 and int(z[1])>0) or not(int(z[2])<10000):
                raise Exception
            x=False
        except:
            print("Please enter a valid date.")
    return z

# function to read files and return dictionary (if line starts with + sign, then that is the the first key in a nested dictionary)
def readFile(filei,records=False):
    # filei refers to the file that needs to be converted to a dictionary, records is to check whether the file that is being converted to a dictionary is the game log
    with open(filei,'r') as fn:
        key1={}
        subkey={}
        z=""
        for line in fn:
            if line[:-1]=="END" or line=="END":
                key1[z]=subkey
                z=""
                subkey={}
            elif line[0]=="+":
                z=line[1:-1]
            elif line!="":
                if records:
                    x=line[:-1].split('|')
                    subkey[f'{x[2]} ({x[1]})']={'date':x[0],'pts':x[3],'words':(x[4].split(','))}
                else:
                    x=line[:-1].split(':')
                    subkey[x[0]]=x[1]
        return key1

# DICTIONARIES
records=readFile("game_log.txt",True)
word_list=readFile("word_list1.txt")
game_settings=readFile("game_settings1.txt")
passwords=readFile('passwords.txt')

# function to return specific lines in record dictionary
def readRecs():
    records=readFile("game_log.txt",True)
    print("\nPlease enter integer dates in this format: dd-mm-yyyy.")
    datei=checkList("Enter First Date: ")
    dateii=checkList("Enter Last date: ")
    print("name\tdate\tpoints\twords")
    if datetime(int(datei[2]),int(datei[1]),int(datei[0]))>datetime(int(dateii[2]),int(dateii[1]),int(dateii[0])):
        first=dateii
        last=datei
    else:
        first=datei
        last=dateii
    print('RECORDS')
    for i in records:
        print(f'\n{i}')
        for names in records[i]:
            curlist=records[i][names]['date']
            points=records[i][names]['pts']
            words=records[i][names]['words']
            current=curlist.split('-')
            curdate=datetime(int(current[2]),int(current[1]),int(current[0]))
            if curdate>=datetime(int(first[2]),int(first[1]),int(first[0])) and curdate<=datetime(int(last[2]),int(last[1]),int(last[0])):
                print(f'{names}\tdate:{curlist}\tpoints:{points}\twords:{words}')
    
# function to add dictionary 
def addnewDic(dic1,newDic):
    # dic1 refers to the dictionary that will be edited, newdic refers to the new dictionary that will be nested in dic1
    dic1[newDic]={}
    records[newDic]={}
    with open('game_log.txt','a') as fn:
        fn.write(f'+{newDic}\n')
        fn.write('END\n')

# funtion to add new item to dictionary
def addtoDic(dic1,key1,key2,val):
    # dic1 refers to the biggest dictionary, key1 refers to the nested dictionary, key2 refers to the new key that will be in key1 and val is the value of key2
    dic1[key1][key2]=val

# function to print keys of dictionary enumerated and return key and value
def printDic(dic1, x=True, y='edit',z=False):
    # dic1 refers to the dictionary to be printed, x refers to ehther the values of the keys in the dictionary should be displayed (False to display), y is a parameter that will alllow you to change 1 word in the prompt and z checks whether you can exit the menu generated by this function
    print("")
    for num,i in enumerate(dic1):
        if x:
            print(f"\t{num+1}) {i}")
        else:
            print(f"\t{num+1}) {i}: {dic1[i]}")
    if z==False:
        print("\nPress Enter to exit.")
    item=checkinRange((f"\nWhat would you like to {y}?\nInput a number: "),num)
    if item=="" and z:
        print("Please enter an integer within the given range.\n")
        a= True
        while a:
            try:
                newitem=checkinRange((f"What would you like to {y}?\nInput a number: "),num)
                if newitem=="":
                    raise Exception
                a=False
                item=newitem
            except:
                print("Please enter an integer within the given range.\n")
    elif item=="":
        return item
    for num,i in enumerate(dic1):
        if (num+1)==int(item):
            return i

# fuction to edit meaning of an item in dictionary
def changeinDic(dic1):
    # dic1 refers to the dictionary which will be edited
    key1= printDic(dic1,z=True)
    if len(dic1[key1])==0:
        print("This dictionary is empty.")
    else:
        key2= printDic(dic1[key1], False,z=True)
        val= input("\nWhat is the new description? ").lower()
        dic1[key1][key2]=val

# fuction to edit an item in dictionary
def changeIteminDic(dic1):
    # dic1 refers to the dictionary which will be edited
    key1= printDic(dic1)
    if key1=="":
        return
    elif len(dic1[key1])==0:
            print("This dictionary is empty.")
    else:
        key2= printDic(dic1[key1], False,z=True)
        newkey= (checkkifvalid()).lower()
        oldval=dic1[key1].pop(key2)
        if checkifinDic(dic1[key1],newkey)=="exists":
            print("This word already exists.")
            dic1[key1][key2]=oldval
        elif len(newkey)<10 and key1=="Complex words":
            print("Word has to be more than 10 letters.")
            dic1[key1][key2]=oldval
        elif key1=="Complex idioms and proverbs":
            numofspaces=0
            for i in newkey:
                if i ==" ":
                    numofspaces+=1
            if numofspaces<7:
                print("Complex idioms and proverbs need to have more than 7 words in them.")
            else:
                dic1[key1][newkey]=oldval
        else:
            dic1[key1][newkey]=oldval
        
        
    
# fucntion to delete an item in a dictionary
def delinDic(dic1):
    # dic1 refers to the dictionary which will be edited
    key1= printDic(dic1)
    if key1=="":
        return
    elif len(dic1[key1])==0:
        print("This dictionary is empty.")
    else:
        key2= printDic(dic1[key1], False, 'delete',True)
        del dic1[key1][key2]

# function to write to file
def writeFile(dic1,filei):
    # dic1 refers to the dictionary that should be written and filei refers the file to which it has to be written to 
    with open(filei,'w') as fn:
        for a in dic1:
            fn.write(f'+{a}\n')
            for b in dic1[a]:
                fn.write(f'{b}:{dic1[a][b]}\n')
            fn.write('END\n')

# texts for adminMain
admintxt="\nWelcome to the admin panel:\n\t1) Edit dictionaries\n\t2) Edit game settings\n\t3) See records\n\t4) Reset password"
dicEdittxt="\n\t1) Add a new dictionary\n\t2) Add a new word to an existing dictionary\n\t3) Edit description of a word in an existing dictionary\n\t4) Delete a word in an existing dictionary\n\t5) Edit a word in an existing dictionary"
settingtxt="\n\t1) Edit number of attempts\n\t2) Edit number of words\n\t3) Edit number of top players"
texta="\n\nPress Enter to exit.\nWhat would you like to choose? "

# function for validating given username and password only
def newpassword():
    x=True
    while x:
        passwd=input("\nPassword must comply with the following:\n- Should have at least one number\n- Should have at least one uppercase and one lowercase character\n- Should have at least one of these special symbols (!@#$%)\n- Should be between 4 to 20 characters long\n\nPlease enter your new password: ")
        num1,up1,low1,spec1=0,0,0,0
        nums,ups,lows,specs='1234567890','ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz','!@#$%^&*()|\\'
        for i in passwd:
            if i in nums:
                num1+=1
            elif i in ups:
                up1+=1
            elif i in lows:
                low1+=1
            elif i in specs:
                spec1+=1
        if num1==0 or up1==0 or low1==0 or spec1==0 or len(passwd)>20:
            print("Password is invalid.") 
        else:
            x=False
            passwords['usernames']['admin']=passwd
    writeFile(passwords,'./passwords.txt')
def checkUser(user,passwd):
    username=input("\033[1;33;40mUsername (Case Sensitive): \033[0;37;40m")
    password=input("\033[1;33;40mPassword (Case Sensitive): \033[0;37;40m")
    if username != user or password!= passwd:
        return True
    else:
        return False

# function to check if the word (key) entered by user contains only valid characters
def checkkifvalid():
    allowedz='abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ\''
    boolean=True
    while boolean:
        key2= input("Enter the new word: ").lower()
        if (all(ch in allowedz for ch in key2)) and key2 !="":
            boolean=False
        else:
            print("All words/idioms/proverbs to be guessed have to only contain letters and the occasional \" \' \"") 
    return key2  

# function with the loop to edit word_list1.txt
def editDicloop():
    a=True
    while a:
        word_list=readFile("./word_list1.txt")
        num2=checkinRange((dicEdittxt+texta),4)
        if num2=="":
            a=False
        elif int(num2)==1:
            key1= input("Enter the name of the new dictionary: ")
            if checkifinDic(word_list,key1)!="exists" and key1!="":
                addnewDic(word_list,key1)
            elif key1=="":
                print("Please enter a name for the dictionary.")
            else:
                print("This dictionary already exists")
        elif int(num2)==2:
            key1= printDic(word_list)
            if key1=="":
                return ""
            else:
                key2=checkkifvalid()
                if checkifinDic(word_list[key1],key2)=="exists":
                    print("This word already exists.")
                elif key1=="Complex words" and len(key2)<10:
                    print("Word has to have more than 10 letters.")
                elif key1=="Complex idioms and proverbs":
                    numofspaces=0
                    for i in key2:
                        if i ==" ":
                            numofspaces+=1
                    if numofspaces<7:
                        print("Complex idioms and proverbs need to have more than 7 words in them.")
                    else:
                        val=input("Enter the description of the new word: ").lower()
                        addtoDic(word_list,key1,key2,val)
                else:
                    val=input("Enter the description of the new word: ").lower()
                    addtoDic(word_list,key1,key2,val)
        elif int(num2)==3:
            changeinDic(word_list)
        elif int(num2)==4:
            delinDic(word_list)
        elif int(num2)==5:
            changeIteminDic(word_list)
        writeFile(word_list,'./word_list1.txt')

# function with loop to edit game_settings1.txt
def editSettingsloop():
    a=True
    while a:
        game_settings=readFile("./game_settings1.txt")
        num3=checkinRange((settingtxt+texta),3)
        if num3=="":
            a=False
        elif int(num3)==1:
            currval=game_settings['game settings']['number of attempts']
            print(f'\nCurrent value is: {currval}')
            val= checkifInt("What is the new value? ")
            game_settings['game settings']['number of attempts']=val
        elif int(num3)==2:
            currval=game_settings['game settings']['number of words']
            print(f'\nCurrent value is: {currval}')
            val= checkifInt("What is the new value? ")
            game_settings['game settings']['number of words']=val
        elif int(num3)==3:
            currval=game_settings['game settings']['number of top players']
            print(f'\nCurrent value is: {currval}')
            val= checkifInt("What is the new value? ")
            game_settings['game settings']['number of top players']=val
        writeFile(game_settings,'./game_settings1.txt')

# function for the main admin panel loop
def adminMain():
    passwords=readFile('./passwords.txt')
    if checkUser('admin',passwords['usernames']['admin']):
        print("Either the username or password is wrong.")
    else:
        x=True
        while x:
            num1= checkinRange((admintxt+texta),3)
            if num1=="":
                x=False
            elif int(num1)==1:
                editDicloop()
            elif int(num1)==2:
                editSettingsloop()
            elif int(num1)==3:
                readRecs()
            elif int(num1)==4:
                newpassword()
