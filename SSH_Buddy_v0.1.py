# SSH Buddy ver 0.1
# Made by Joe Issa
#this tool is supposed to help you get your linux SSH connection command ready.
TIP = input("Please enter target ip :")
TUS = input("Please enter target username :")
PVTKEY = input("Do you have the Target Private Key ? ")
if PVTKEY == "yes":
    PVTKEYLOC = input("please enter the full location of the Private key")
    print("thank you !")
elif PVTKEY == "no":
    PVTKEYLOC = 0
    print("ok so no key ... no biggie")
else:
    print("please answer with a yes or no")

if PVTKEYLOC == 0:
    print("ssh",TUS+"@"+TIP)
elif PVTKEYLOC != 0:
    print("ssh -i",PVTKEYLOC,TUS+"@"+TIP)
else:
    print("something is wrong ,just do it yourself !")
