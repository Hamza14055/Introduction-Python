Pass = str(input("Which password do you want to set ? "))
if not('a' in Pass) :
    print("The password must contain the letter 'a' ")
elif 'a' in Pass :
    print("Password Set successfully")