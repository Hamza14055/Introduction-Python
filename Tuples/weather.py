weather = (1, 0, 0, 0, 1, 1, 0)
sunny = 0 
rainy = 0 
for i in range (0,7):
    if weather [i] == 0:
        sunny+=1
    elif weather[i] == 1:
        rainy +=1
print("The chances of weather being sunny is ",sunny,"chances of rainy is",rainy)