#create a dictionary in which keys will be the location or position
theBoard={'7': ' ', '8': ' ', '9': ' ',
          '4': ' ', '5': ' ', '6': ' ',
          '1': ' ', '2': ' ', '3': ' '}

#create a function to print the updated board after every move in the game 
def printBoard(board):
    print(board['7']+'|'+ board['8']+'|'+ board['9'])
    print('-+-+-')
    print(board['4']+'|'+ board['5']+'|'+ board['6'])
    print('-+-+-')
    print(board['1']+'|'+ board['2']+'|'+ board['3'])

#create a function which has all the gameplay functionality
def game():
    
    turn='x'#create a turn variable and assign it "x",always tic tac toe game starts with x
    
    count=0 #create a variable "count" and use this variable to count the no of moves of both the players
    
    for i in range(10): # create a for loop with range function with arg<10 bcoz we need to execute the player turn for 9 times
    
        printBoard(theBoard)#print board using function
    
        print("IT IS YOUR TURN,"+turn+". CHOOSE YOUR PLACE")
    
        move=input()# use input() to get the input
    
        if theBoard[move]==' ':# use if-else statement find the empty place on board(dictionary)
      
           theBoard[move]=turn
      
           count +=1
      
        else:
      
            print("THE PLACE IS ALREADY FILLED...:(") 
      
            continue   
      
        if count >=5: #Now use if elif statement to check every possible win conction
      
           if theBoard['7']==theBoard['8']==theBoard['9']!=' ':
      
              printBoard(theBoard)
      
              print("\nGAME OVER...\n")
      
              print("****" +turn + "WON..****")
      
              break
      
           elif theBoard['4']==theBoard['5']==theBoard['6']!=' ':
      
              printBoard(theBoard)
      
              print("\nGAME OVER...\n")
      
              print("****" +turn + "WON..****")
      
              break
      
           elif theBoard['1']==theBoard['2']==theBoard['3']!=' ':
      
              printBoard(theBoard)
      
              print("\nGAME OVER...\n")
      
              print("****" +turn + "WON..****")
      
              break
      
           elif theBoard['1']==theBoard['4']==theBoard['7']!=' ':
      
              printBoard(theBoard)
      
              print("\nGAME OVER...\n")
      
              print("****" +turn + "WON..****")
      
              break
      
           elif theBoard['2']==theBoard['5']==theBoard['8']!=' ':
      
              printBoard(theBoard)
      
              print("\nGAME OVER...\n")
      
              print("****" +turn + "WON..****")
      
              break
      
           elif theBoard['3']==theBoard['6']==theBoard['9']!=' ':
      
              printBoard(theBoard)
      
              print("\nGAME OVER...\n")
      
              print("****" +turn + "WON..****")
      
              break
      
           elif theBoard['7']==theBoard['5']==theBoard['3']!=' ':
      
              printBoard(theBoard)
      
              print("\nGAME OVER...\n")
      
              print("****" +turn + "WON..****")
      
              break
      
           elif theBoard['1']==theBoard['5']==theBoard['9']!=' ':
      
              printBoard(theBoard)
      
              print("\nGAME OVER...\n")
      
              print("****" +turn + "WON..****")
      
              break
      
           if count==9:# create if statement to check if neither x nor 0 wins
      
              print("/nGAME OVER...:(\n")
      
              print("Its a Tie!!!")
      
              break
      
           if turn=='x':# now change value of "turn" variable(the player) after every move 
      
              turn='o'
      
           else:
      
             turn='x'

game()# calling the game() function to execute             






