def square_list():
    star = int(input("Enter the starting number "))
    en = int(input("Enter the ending number "))+1
    for i in range (star,en):
        square = i*i
        if square%2 == 0 :
            print("Even square ",square)
        else:
            print("Odd square ",square)
square_list()