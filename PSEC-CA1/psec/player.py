'''
Main Program

StudentID: P2227171
Name: Swaathi Lakshmanan
Class: DISM/FT/1B/05
Assessment: CA1-1

Script name:
player.py

Purpose: 
This is the main program for the whole hangman game. Links admin.py with the main game menu, and contains the script for the game itself.

Usage Syntax:
Run with command line: python .\player.py

Input files:
d:/psec/game_log.txt
d:/psec/game_settings1.txt
d:/psec/hangman_hanged.txt
d:/psec/passwords.txt
d:/psec/word_list1.txt

Output files:
d:/psec/game_log.txt
d:/psec/passwords.txt

Python version:
Python 3

Reference:
None (to download)

Library/Module:
None

Known issues:
None
'''
# imports
import admin
import random
import datetime
import copy

# texts
alloweds='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/-'
anothersectxt="Either you have covered this section or there only limited words in this section. Please choose another one if you would like to play."
allowedz='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\'12'
playagaintxt="Enter [N] to quit (Enter any character to continue): "
texta="\n\nPress Enter to end.\nWhat would you like to choose? "

# dictionaries
records=admin.readFile("game_log.txt",True)
word_list=admin.readFile("word_list1.txt")
game_settings=admin.readFile("game_settings1.txt")
passwords=admin.readFile('passwords.txt')

# functions

# functions to check for username
def firstUsername():
    passwords=admin.readFile('passwords.txt')  
    x=True
    while x:
        y=True
        print("\nYou can create a new username (and new password) or use an existing username (with existing password)")
        username=input("\033[1;32;40mUsername (Case Sensitive): \033[0;37;40m")
        passwd=input("\033[1;32;40mPassword (Case Sensitive): \033[0;37;40m")
        for i in passwords['usernames']:
            if i == username:
                if passwd==passwords['usernames'][i]:
                    print("\nLogged in.")
                    x=False
                    break
                else:
                    print("If you are trying to login, your password is incorrect. If you are trying to create a new username, the username already exists.")
                    y=False
        else:
            if not(all(ch in alloweds for ch in username)) or username=="":
                print("invalid username.")
            elif y:
                x=False
                print("\nUsername created.")
                passwords['usernames'][username]=passwd
                admin.writeFile(passwords,"./passwords.txt")
    return username

# function to generate unique words for game
def randomword(section,username):
    # section refers to the category of words the player wants to play and username refers to the username of the player
    records=admin.readFile("game_log.txt",True)
    word_list=admin.readFile("word_list1.txt")
    game_settings=admin.readFile("game_settings1.txt")
    numattempts= int(game_settings['game settings']['number of attempts'])
    numwords= int(game_settings['game settings']['number of words'])
    usedWords=[]
    for i in records[section]:
        if i[:-4]==username:
            usedWords.extend(records[section][i]['words'])
    copydic=copy.deepcopy(word_list[section])
    for i in usedWords:
        del copydic[i]
    if len(copydic)<(numattempts*numwords):
        return anothersectxt
    else:
        newwords=random.sample(range(len(copydic)),(numattempts*numwords))
        newwordlist=[]
        for num in newwords:
            for index,i in enumerate(copydic):
                if index==num:
                    newwordlist.append(i)
        return newwordlist

# function to write records list to file
def writeRecords():
    with open('game_log.txt','w') as fn:
        for a in records:
            fn.write(f'+{a}\n')
            for b in records[a]:
                date=records[a][b]['date']
                pts=records[a][b]['pts']
                words=""
                for i in records[a][b]['words']:
                    words+=f"{i},"
                fn.write(f'{date}|{b[-2]}|{b[:-4]}|{pts}|{words[:-1]}\n')
            fn.write('END\n')

# function to find the number of games a username played and add new game data to dictionary
def numofgames(username,points,words,section):
    # username refers to the username of the player, points refers to the points the player scored in the game and section refers to the catgory which the player played
    num=0
    for i in records[section]:
        if i[:-4]==username:
            num=int(i[-2])
    curr=datetime.datetime.now()
    date,month,year=curr.strftime("%d"),curr.strftime("%m"),curr.strftime("%Y")
    currentdate=f"{date}-{month}-{year}"
    records[section][f'{username} ({num+1})']={'date':currentdate,'pts':str(points),'words':words}
    writeRecords()

# function to print hangman
fn=open('./hangman_hanged.txt','r')
contents=fn.readlines()
fn.close()
def printMan(n):
    for i in contents[((n-1)*10):(n*10)]:
        print(i[:-1])

# function for main game.
def hangtheman(wordlist,username,section):
    # wordlist refers to the words generated for the player to play, useername refers to username of the player, and section refers to the category the player is playing
    game_settings=admin.readFile("game_settings1.txt")
    word_list=admin.readFile("word_list1.txt")
    points=0
    currentpoints=0
    allowedc=[]
    playagain="a"
    donewords=[]
    for i in allowedz:
        allowedc.append(i)
    numattempts= int(game_settings['game settings']['number of attempts'])
    numwords= int(game_settings['game settings']['number of words'])
    helpline=['show all vowels','show meaning of item']
    for i in range(numattempts):
        if playagain=="n":
            break
        print(f"\nPlayer:{username}")
        print(f"Attempt {i+1} of {numattempts}\n")
        wordset=wordlist[(i*numwords):((i+1)*numwords)]
        allowedsub=allowedc[:]
        for index in range(numwords):
            if playagain=="n":
                break
            currentpoints=0
            print(f"word {index+1}\n")
            theWord=wordset[index]
            donewords.append(theWord)
            blanklist=[]
            for i in theWord:
                if i == " ":
                    blanklist.append(' ')
                else:
                    blanklist.append('_')
            x=True
            hangnum=1
            wrongl=[]
            correctguesses=0
            while x:
                printMan(hangnum)
                print(f"Incorrect letters:",end=" ")
                [print(ch, end=" ") for ch in wrongl]
                print(f"({len(wrongl)})")
                [print(ch, end=" ") for ch in blanklist]
                print("\n")
                if len(allowedsub)>53:
                    print('\nHELPLINE (only one per attempt):')
                    [print(f'{number+1}) {string}') for number,string in enumerate(helpline)]
                y=True
                isnum=True
                loophole=True
                while y: 
                    guess=input("Select a valid letter [a-z,']: ").lower()
                    if not(all(ch in allowedsub for ch in guess)) or (len(guess)>1) or guess=="":
                        print("Invalid letter")
                        y=True
                    elif guess.isnumeric():
                        loophole=False
                        if helpline[int(guess)-1]=='show all vowels':
                            vowels=['a','e','i','o','u']
                            for i in range(len(blanklist)):
                                for chs in vowels:
                                    if chs==theWord[i]:
                                        blanklist[i]=theWord[i]
                            currentpoints-=4
                            helpline.pop(0)
                        else:
                            print(f'The meaining is: {word_list[section][theWord]}')
                            currentpoints-=4
                            helpline.pop()
                        allowedc.pop()
                        allowedsub=allowedsub[:-2]
                        y=False 
                    else:
                        y=False     
                iscorrect=False
                incase=True
                if isnum:
                    for i in range(len(blanklist)):
                        if guess==theWord[i]:
                            if guess==blanklist[i]:
                                incase=False
                            iscorrect=True
                            blanklist[i]=theWord[i]       
                if iscorrect:
                    if incase:
                        correctguesses+=1
                        currentpoints+=1
                    if currentpoints>19:
                        currentpoints=19
                elif loophole:
                    wrongl.append(guess)
                    hangnum+=1
                playagain,x,ifwin,currentpoints=checkifwin(blanklist,hangnum,wrongl,section,theWord,currentpoints)
                if ifwin==False:
                    playagain,x,iflose=checkiflose(hangnum,wrongl,blanklist,correctguesses,theWord,section)
                if ifwin or iflose:
                    x=False
            points+=currentpoints
    print(f"Your points for this game: \033[1;32;40m{points}\033[0;37;40m")
    numofgames(username,points,donewords,section)


# function to check if player won the game
def checkifwin(blanklist,hangnum,wrongl,section,theWord,currentpoints):
    # blanklist refers to list which includes the correct letters the player guessed, hangnum refers to the latest hangman picture, wrong1 refers to the incorrect letters, section refers to the cateegory the player is playing, theWord refers to the word the player is trying to guess and current points refers to the points the user has earned so far.
    word_list=admin.readFile("word_list1.txt")
    ifwin=True
    for char in blanklist:
        if char=="_":
            ifwin=False
    if ifwin:
        printMan(hangnum)
        print(f"Incorrect letters:",end=" ")
        [print(ch, end=" ") for ch in wrongl]
        print(f"({len(wrongl)})")
        [print(ch, end=" ") for ch in blanklist]
        print("\n")
        print(f"\033[1;36;40mCongratulations. The secret {section} is {theWord}: {word_list[section][theWord]}\033[0;37;40m")
        playagain=input(playagaintxt).lower()
        return playagain, False, True,20
    else:
        return 'a', True, ifwin,currentpoints

# function to check if player lost the game
def checkiflose(hangnum,wrongl,blanklist,correctguesses,theWord,section):
    # blanklist refers to list which includes the correct letters the player guessed, hangnum refers to the latest hangman picture, wrong1 refers to the incorrect letters, section refers to the cateegory the player is playing, theWord refers to the word the player is trying to guess and correctguess refers to the number of correct guess the player has made so far.
    word_list=admin.readFile("word_list1.txt")
    if hangnum==7:
        printMan(hangnum)
        print(f"Incorrect letters:",end=" ")
        [print(ch, end=" ") for ch in wrongl]
        print(f"({len(wrongl)})")
        [print(ch, end=" ") for ch in blanklist]
        print("\n")
        print(f'\033[1;31;40mMaximum number of guesses!\nAfter {len(wrongl)} guesses and {correctguesses} correct guess(es) the word was {theWord}: {word_list[section][theWord]}\033[0;37;40m')
        playagain=input(playagaintxt).lower()
        return playagain, False,True
    else:
        return 'a',True,False

# function to print top players in a game (but function only returns top players)
def printTop(section):
    # section refers to the category the user is playing
    records=admin.readFile("game_log.txt",True)
    numtop= int(game_settings['game settings']['number of top players'])
    subdic=copy.deepcopy(records)
    printstr,curindex="",""
    for i in range(numtop):
        if curindex!="":
            del subdic[section][curindex]
        points=0
        tempstr=""
        curindex=""
        for index in subdic[section]:
            if int(subdic[section][index]['pts'])>int(points):
                curindex=index
                points=subdic[section][index]['pts']
                curlist=records[section][index]['date']
                tempstr=f'{i+1}.{index}\tdate:{curlist}\tpoints:{points}\n'
        printstr+=tempstr
    return printstr


# Welcome text
intialinput= "\033[1;32;40m\nWelcome to Hangman (Swaathi's version)!\033[0;37;40m\n\t1. Play a game\n\t2. Go to Admin panel"

# function for main game loop
def game():
    x=True
    while x:
        num1=admin.checkinRange((intialinput+texta),2)
        if num1=="":
            x=False
            print('Thank you.')
        elif int(num1)==1:
            word_list=admin.readFile("word_list1.txt")
            username=firstUsername()
            passwords=admin.readFile("./passwords.txt")
            section=admin.printDic(word_list, x=True, y='choose')
            if section!="":
                wordlist=randomword(section,username)
                if type(wordlist)==list:
                    print("\nH A N G M A N <3")
                    hangtheman(wordlist,username,section)
                    writeRecords()
                    print(f'\nTop Players for {section}')
                    print(printTop(section))
                else:
                    print(wordlist)
        elif int(num1)==2:
            admin.adminMain()
            

# Actual function that runs
game()