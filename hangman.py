import random

#function
def guessWord():
    score=0
    secret=""
    print("Guess the word!")
    lives=7
    word=random.randint(0,len(words))
    while lives!=0:
        var=0
        print("")
        for i in words[word]:
            if i in secret:
                print (i,end="")
            elif i==" ":
                print (" ",end="")
            elif i==":":
                print (":",end="")
            elif i=="-":
                print ("-",end="")
            elif i=="!":
                print ("!",end="")
            elif i==".":
                print (".",end="")
            elif i=="?":
                print ("?",end="")
            else:
                print ("▐▌",end="")
                var=var+1
    
        if var==0:  
            print("")
            print("\n"+"Correct! The word is", words[word])
            break
        
        guess=input("\n"+"Guess a letter: ")
        secret=secret+guess

        if guess not in words[word]:
            lives=lives-1
            print ("Wrong")
            print("You have",+lives,"turn/s left")
            if lives==7:
                print("")
                print("")
                scores=score+100
            elif lives==6:
                print(">")
                print("")
                scores=score+90
            elif lives==5:
                print(">-")
                print("")
                scores=score+80
            elif lives==4:
                print(">--")
                print("")
                scores=score+70
            elif lives==3:
                print(">--|")
                print("")
                scores=score+60
            elif lives==2:
                print(">--|-")
                print("")
                score=score+50
            elif lives==1:
                print(">--|--")
                print("")
                scores=score+30
            elif lives==0:
                print(">--|--O")
                print("")
                print ("Wrong!")
                print("")
                scores=0
                print ("\n"+"The word is", words[word])
                break
    return str(scores)

#main program
pick="a"
print ("Welcome to Hangman!")
print (">--|--O")
x=input("Please enter name: ")
while pick!="c":
    print ("")
    print("A. PLAY                  C. EXIT")
    print("B. VIEW SCORES")
    pick=input("What do you want to do? ")
    print ("")
    if pick=="a" or pick=="A":
        print("a. Animals")
        print("b. Anime")
        print("c. Scientists")
        print("")
        print("BACK")
        cat=input("Please choose a category: ")
        print ("")
        if cat=="a":
            print("a. Easy")
            print("b. Medium")
            print("c. Hard")
            choice=input("Choose a dificulty: ")
            print ("")
            if choice=="a":
                fileReader=open ("easya.txt","r")
                for line in fileReader:
                    words=line.split(",")
                fileReader.close()
                fileWriter=open ("easyah.txt","a")
                fileWriter.write("\n"+x+"-"+guessWord()+"\n")
                fileWriter.close()
            elif choice=="b":
                fileReader=open("mediuma.txt","r")
                for line in fileReader:
                    words=line.split(",")
                fileReader.close()
                fileWriter=open ("mediumah.txt","a")
                fileWriter.write("\n"+x+"-"+guessWord()+"\n")
                fileWriter.close()
            elif choice=="c":
                fileReader=open ("harda.txt","r")
                for line in fileReader:
                    words=line.split(",")
                fileReader.close()
                fileWriter=open ("hardah.txt","a")
                fileWriter.write("\n"+x+"-"+guessWord()+"\n")
                fileWriter.close()  
            else:
                print("Invalid choice")
        elif cat=="b":
            print("a. Easy")
            print("b. Medium")
            print("c. Hard")
            choice=input("Choose a dificulty: ")
            print ("")
            if choice=="a":
                fileReader=open ("easye.txt","r")
                for line in fileReader:
                    words=line.split(",")
                fileReader.close()
                fileWriter=open ("easyeh.txt","a")
                fileWriter.write("\n"+x+"-"+guessWord()+"\n")
                fileWriter.close()
            elif choice=="b":
                fileReader=open("mediume.txt","r")
                for line in fileReader:
                    words=line.split(",")
                fileReader.close()
                fileWriter=open ("mediumeh.txt","a")
                fileWriter.write("\n"+x+"-"+guessWord()+"\n")
                fileWriter.close()
            elif choice=="c":
                fileReader=open ("harde.txt","r")
                for line in fileReader:
                    words=line.split(",")
                fileReader.close()
                fileWriter=open ("hardeh.txt","a")
                fileWriter.write("\n"+x+"-"+guessWord()+"\n")
                fileWriter.close()
            else:
                print("Invalid choice")
        elif cat=="c":
            print("a. Easy")
            print("b. Medium")
            print("c. Hard")
            choice=input("Choose a dificulty: ")
            print ("")
            if choice=="a":
                fileReader=open ("easys.txt","r")
                for line in fileReader:
                    words=line.split(",")
                fileReader.close()
                fileWriter=open ("easysh.txt","a")
                fileWriter.write("\n"+x+"-"+guessWord()+"\n")
                fileWriter.close()
            elif choice=="b":
                fileReader=open("mediums.txt","r")
                for line in fileReader:
                    words=line.split(",")
                fileReader.close()
                fileWriter=open ("mediumsh.txt","a")
                fileWriter.write("\n"+x+"-"+guessWord()+"\n")
                fileWriter.close()
            elif choice=="c":
                fileReader=open ("hards.txt","r")
                for line in fileReader:
                    words=line.split(",")
                fileReader.close()
                fileWriter=open ("hardsh.txt","a")
                fileWriter.write("\n"+x+"-"+guessWord()+"\n")
                fileWriter.close()
            else:
                print("Invalid choice")
        else:
            continue
    elif pick=="b" or pick=="B":
        print("a. Animals")
        print("b. Anime")
        print("c. Scientists")
        print("")
        print("BACK")
        cat=input("Please choose a category you want to view: ")
        print ("")
        if cat=="a":
            fileReader=open ("easyah.txt","r")
            for line in fileReader:
                line=line[:-1]
                print (line)
            fileReader.close()
            fileReader=open ("mediumah.txt","r")
            for line in fileReader:
                line=line[:-1]
                print (line)
            fileReader.close()
            fileReader=open ("hardah.txt","r")
            for line in fileReader:
                line=line[:-1]
                print (line)
            fileReader.close()
        elif cat=="b":
            fileReader=open ("easyeh.txt","r")
            for line in fileReader:
                line=line[:-1]
                print (line)
            fileReader.close()
            fileReader=open ("mediumeh.txt","r")
            for line in fileReader:
                line=line[:-1]
                print (line)
            fileReader.close()
            fileReader=open ("hardeh.txt","r")
            for line in fileReader:
                line=line[:-1]
                print (line)
            fileReader.close()
        elif cat=="c":
            fileReader=open ("easysh.txt","r")
            for line in fileReader:
                line=line[:-1]
                print (line)
            fileReader.close()
            fileReader=open ("mediumsh.txt","r")
            for line in fileReader:
                line=line[:-1]
                print (line)
            fileReader.close()
            fileReader=open ("hardsh.txt","r")
            for line in fileReader:
                line=line[:-1]
                print (line)
            fileReader.close()
        else:
            print("Invalid choice")
    else:
        break
