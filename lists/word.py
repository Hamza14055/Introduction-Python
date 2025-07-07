def same_word(word):
    ctr = 0
    my_list=[]
    for i in word:
        if len(i)>1 and i[0] == i[-1]:
            ctr +=1
            my_list.append(i)
            
    print("The list with same last and first character is : ",my_list)
    return ctr 
print("the words with same first and last character are ",same_word(["abc","abba","cfc","dab"]))
