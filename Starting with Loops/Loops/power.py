Num = int(input("enter the number : "))
power = 1
power_2 = int(input("enter the desired power : "))
while power != power_2:
    power = power + 1
print(Num,'^',power_2,'=',Num**power)