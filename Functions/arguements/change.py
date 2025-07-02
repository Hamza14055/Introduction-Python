n = int(input("Enter the total ammount "))
i = int(input("Enter the ammount you paid "))
def change():
    ret = n - i
    return ret
print("The change is ",change())