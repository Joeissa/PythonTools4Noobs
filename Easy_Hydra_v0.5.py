# Easy Hydra ver0.5
# made by Joe Issa
# Easy Hydra is here to help you with the damn syntax !
# Currently work only with SSH and FTP
import os
from subprocess import run

def easyhydra():
    TIP = input("Please Enter The Target IP : ")
    print("Currently this tool supports only ssh and ftp services ")
    Service = input("What do you want to bruteforce ? (ssh or ftp) : ")
    if Service == "ssh":
        print("ssh it is !")
    elif Service == "ftp":
        print("ftp it is !")
        print("PS: You can try to login as anonymous")
    else:
        print("Unknown service or you are trying to be a smartass")
        exit()

    user = input("do you have a username ? (yes or no) :  ")
    if user == "yes":
        usery = input("please enter username : ")
    elif user == "no":
        userl = input("please enter a username list path")
        pathu = os.path.abspath(userl)
    else:
        print("please answer with a yes or no")
        exit()

    passw = input("do you have a password ? (yes or no) :  ")
    if passw == "yes":
        passwy = input("please enter the password : ")
    elif passw == "no":
        passwl = input("please enter a wordlist location : ")
        pathp = os.path.abspath(passwl)
    else:
        print("please answer with a yes or no")
        exit()


    if user == "yes" and passw == "yes":
        noob = input("you already have the credentials , what service do you need ? (ssh or ftp)")
        if noob == "ssh":
            run(["ssh",usery+"@"+TIP])
            exit()
        elif noob == "ftp":
            run(["ftp",TIP])
            exit()
        else:
            print("something is wrong , please try again")
            exit()

    if user == "yes" and passw == "no":
        run(["hydra","-l",usery,"-P",pathp,Service+"://"+TIP])
    elif user == "no" and passw == "yes":
        run(["hydra","-L",pathu,"-p",passwy,Service+"://"+TIP])
    else:
        print("this will take for ever , there must be another way !")
        exit()
easyhydra()
