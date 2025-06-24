def shutdown():
    confirm = input("Do you want to shutdown the computer Yes/No : ")
    if confirm.lower() == "yes":
        programs = input("Are there any programs running Yes/No : ")
        if programs.lower()== "yes":
            print("Please shut down all programs before shutting down !")
        elif programs.lower() == "no" :
            print("Shutting down ... ")
    elif confirm.lower() == "no":
        print("Pc will not shutdown ")
    else:
        print("Enter only Yes or No ")


shutdown()