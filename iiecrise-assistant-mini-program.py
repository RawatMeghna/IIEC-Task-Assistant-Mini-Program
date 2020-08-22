import os
def task(p):
    if(("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("chrome" in p) or ("google" in p)):
        return("1")
    elif(("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("notepad" in p)or("notebook" in p)or("editor" in p)):
        return("2")
    elif(("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("explorer" in p) or ("browser" in p)):
        return("3")
    elif(("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("media" in p) or ("player" in p)):
        return("4")
    elif(("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("calculator" in p) or ("calc" in p)):
        return("5")
    elif(("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("powerpoint" in p) or ("mspowerpoint" in p)):
        return("6")
    elif(("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("paint" in p) or ("drawing" in p)):
        return("7")
    elif(("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("msword" in p) or ("wordpad" in p)):
        return("8")
    elif(("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("excel" in p) or ("sheets" in p)):
        return("9")
    elif(("exit" in p) or ("quit" in p)):
        return("10")
    else:
        return("Incorrect command.")
print("Welcome to IIEC Task Assistant Program.")
while True:
    print("Write a command that you want me to perform for you.")
    s=input()
    a=task(s)
    if(a=="1"):   
        print("Opening Chrome for you.")
        os.system("start chrome")
    elif(a=="2"):
        print("Opening Notepad for you.")
        os.system("start notepad")
    elif(a=="3"):
        print("Opening Internet Explorer for you.")
        os.system("start iexplore")
    elif(a=="4"):
        print("Opening Window Media Player for you.")
        os.system("start wmplayer")
    elif(a=="5"):
        print("Opening Calculator for you.")
        os.system("start calc")
    elif(a=="6"):
        print("Opening PowerPoint powerpnt")
    elif(a=="7"):
        print("Opening Paint for you.")
        os.system("start mspaint")
    elif(a=="8"):
        print("Opening MS Word for you.")
        os.system("start write")
    elif(a=="9"):
        print("Opening MS Excel for you.")
        os.system("start excel")
    elif(a=="10"):
        print("Okay, bye. Thanks for visiting.")
        break
    else:
        print("Try again!")
