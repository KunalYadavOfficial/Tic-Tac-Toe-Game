#-------Global Variable-----

# board
board=["-","-","-",
       "-","-","-",
       "-","-","-",]

#game status
game_still_going = True

#winner
winner = None
 
current_player ="X"



def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])

#Game start
def play_game():

       display_board()

       while game_still_going:
              
              handle_turns(current_player)         

              check_if_game_over()

              flip_player()
       if winner=="X" or winner=="Y":
              print(winner+" won.")
       elif winner == None:
              print("Tie")       
                     
              
#handle the turn of single player
def handle_turns(player):
       print(player+"'s turn.")

       position=input("enter the position from 1-9: ")


       valid=False
       while not valid:
              #check for invalid input 
              while  position not in ["1","2","3","4","5","6","7","8","9"]:
                     position=input("enter the position from 1-9: ")       
              
              position=int(position)-1
              #check if the position is not acquired already1

              if board[position]=="-":
                     valid=True
              else:
                     print("You cannot go to that position as it is not available.")       
       board[position]=current_player
       display_board()


#check if the game is over or not
def check_if_game_over():
       check_win()
       check_tie()


#check the win status
def check_win():
       #set up the global variables
       global winner

       
       #check row
       row_winner=check_row()
       #check cloumn
       column_winner=check_column()
       #check diagonal
       diagonal_winner = check_diagonal()
       
       #get the winner
       if row_winner:
              winner = row_winner

       elif column_winner:
              winner = column_winner

       elif diagonal_winner:
              winner =  diagonal_winner
       else:
              winner = None            
         


def check_row():

       #setting up global variable
       global game_still_going

       #check if any row has all 3 element same
       row_1=board[0]==board[1]==board[2]!="-"
       row_2=board[3]==board[4]==board[5]!="-"
       row_3=board[6]==board[7]==board[8]!="-"
       if row_1 or row_2 or row_3:
              game_still_going = False    #set game status false
       
       #Get the winner(X or O)
       if row_1:
              return board[0]
       elif row_2:
              return board[3]       
       elif row_3:
              return board[6]


def check_column():

       #setting up global variable
       global game_still_going

       column_1=board[0]==board[3]==board[6]!="-"
       column_2=board[1]==board[4]==board[7]!="-"
       column_3=board[2]==board[5]==board[8]!="-"
       if column_1 or column_2 or column_3:
              game_still_going = False
       
       #Get the winner(X or O)
       if column_1:
              return board[0]
       elif column_2:
              return board[1]       
       elif column_3:
              return board[2]


def check_diagonal():

       #setting up global variable
       global game_still_going

       #if diagonal have a match,then set the flag value
       diagonal_1=board[0]==board[4]==board[8]!="-"
       diagonal_2=board[2]==board[4]==board[6]!="-"
       if diagonal_1 or diagonal_2:
              game_still_going = False
       
       #Get the winner(X or O) 
       if diagonal_1:
              return board[0]
       elif diagonal_2:
              return board[2]



def check_tie():
       
       #settting up global varibale
       global game_still_going
       if "-" not in board:          #when no winner and no space lift on the 
              game_still_going = False

       return


def flip_player():  

       #setting up global varible
       global current_player

       #change player's turn
       if current_player=="X":
              current_player="O"
       elif current_player=="O":
              current_player="X"         



play_game()  

