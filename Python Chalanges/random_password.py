import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "12345678"
Password = ""
for i in range (4):
    Password += random.choice(numbers)  
    Password+=random.choice(letters)

print("A good and secure Passsword is ", Password)