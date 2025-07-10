def check_palindrome(sequence):
    start = 0 
    end = len(sequence)-1
    while start<end :

     if sequence[start] != sequence[end]:
        return False
     start+=1
     end-=1
    
    return True
tuple_1 = (1,2,3,4,5,6)
if check_palindrome(tuple_1):
   print("its a palindrome")
else:
   print("Its not a palindrome")
check_palindrome(tuple_1)
    