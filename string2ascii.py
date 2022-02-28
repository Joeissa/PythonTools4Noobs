print("\033[1;33;40mthis tool converts your input to its ascii value \n")
text = input("please enter the text: ")
ascii = [ord(character) for character in text]
print("Your input ascii value is :",ascii)
