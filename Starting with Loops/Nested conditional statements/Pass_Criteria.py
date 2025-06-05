Password = input("Please enter your new Password ")
if len(Password) < 6 :
    print("The password must be longer than 6 characters ")
    if len(Password) > 16 :
        print("Enter a password smaller than 16 characters ")
    else :
        if not(int in Password ) :
            print("Please enter atleast 1 digit")
        else:
            if not('$','#','@' in Password):
                print("There should be atleast 1 special character : $,#,@")
                if not(Password.isupper()) :
                    print("Please enter atleast 1 uppercase character")
                if not(Password.islower()):
                    print("Please enter atleast 1 lowercase character")
else:
    print("Nice password")


