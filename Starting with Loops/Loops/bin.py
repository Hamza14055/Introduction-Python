A = int(input('Enter A Number '))
Remainder =""
while A>0:
    Remainder = A%2
    A = A//2
    Binary = str(Remainder)+A
Remainder[::-1]
print(Remainder)
