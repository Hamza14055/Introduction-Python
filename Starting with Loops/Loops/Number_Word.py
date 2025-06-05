Word = input("Enter the word ")
Word_Count = 1 
for i in range(len(Word)) :
    if Word [i] == " " :
        Word_Count=Word_Count+1
        
print("Number of words in this sentence are ", Word_Count )
 