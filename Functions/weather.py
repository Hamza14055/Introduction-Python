def weather(season):
    if season.lower() == "autumn":
        print("Its a dry weather ")
    elif season.lower()=="spring":
        print("Its a pleasant weather ")
User = input("Enter the season ")
weather(User)