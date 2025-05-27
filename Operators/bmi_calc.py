Weight = float(input("What is your current weight in Kg ? "))
Height = float(input("What is your current height in cm ? "))
BMI = Weight/(Height/100)**2
if BMI<= 18.4 :
    print("You are underweight ! ")
elif BMI>18.4 and BMI<= 24.9 :
    print("You are healthy ! ")
elif BMI>24.9 and BMI<=29.9 :
    print("You are overweight ! ")
elif BMI>29.9 and BMI <= 34.9 :
    print("You are obese ! ")
else :
    print("You are severely obese ! ")
