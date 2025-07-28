the_board = {'7':' ','8':' ','9':' ',
             '4':' ','5':' ','6':' ',
             '1':' ','2':' ','3':' '}
board_keys =[]
for keys in the_board:
    board_keys.append(keys)
def printBoard(Board):
    print(Board['7']+'|'+Board['8']+'|'+Board['9'])
    print("-+-+-")
    print(Board['4']+'|'+Board['5']+'|'+Board['6'])
    print("-+-+-")
    print(Board['1']+'|'+Board['2']+'|'+Board['3'])
def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(the_board)
        print("Its Your turn"+turn+" move to which place : ")
        move = input()
        if the_board[move]==' ':
            the_board[move]=turn
            count+=1
        else:
            print("That place is already filled./n Move to which place")
            continue 
        if count>= 5 :
            if the_board['7']== the_board['8']==the_board['9']!='':
                printBoard(the_board)
                print("\n Game Over \n")
                print("****"+turn+"won"+"*****")
                break
            elif the_board['4']==the_board['5']==the_board['6']!=' ':
                print("\n Game Over \n")
                print("****"+turn+"won"+"****")
            elif the_board['1']==the_board['2']==the_board['3']!=' ':
                print("\n Game Over \n")
                print("****"+turn+"won"+"****")
            elif the_board['1']==the_board['4']==the_board['7']!=' ':
                print("\n Game Over \n")
                print("****"+turn+"won"+"****")
            elif the_board['2']==the_board['5']==the_board['8']!=' ':
                print("\n Game Over \n")
                print("****"+turn+"won"+"****")
            elif the_board['3']==the_board['6']==the_board['9']!=' ':
                print("\n Game Over \n")
                print("****"+turn+"won"+"****")
            elif the_board['7']==the_board['5']==the_board['3']!=' ':
                print("\n Game Over \n")
                print("****"+turn+"won"+"****")
            elif the_board['1']==the_board['5']==the_board['9']!=' ':
                print("\n Game Over \n")
                print("****"+turn+"won"+"****")
            break
        if count == 9 :
            print("\n Game Over \n")
            print("\n Its a Tie!! \n")
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    restart = input("Do You want to play again Y/N ")
    if restart.upper()== 'Y':
         for keys in board_keys:
                the_board[keys]=" "
         game()
if __name__ =="__main__":
    game()