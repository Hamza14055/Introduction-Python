Word = str(input("which word do you want to check ? "))
if 'a' in Word or 'e' in Word or 'i' in Word or 'o' in Word or 'u' in Word :
    print("This word contains vowels")
elif not('a' in Word or 'e' in Word or 'i' in Word or 'u' in Word or 'o' in Word ):
    print("This contains consonants")