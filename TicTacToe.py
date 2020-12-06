# Create the board using a dictionary
Tic_Tac_Toe_Board ={'1': '', '2': '', '3': '',
                    '4': '', '5': '', '6': '',
                    '7': '', '8': '', '9': ''}

ttt_board_keys = []

for key in Tic_Tac_Toe_Board:
    ttt_board_keys.append(key)


# Create a function that will allow you to view the board at any time.
def print_tic_tac_toe_board(board):
    print(board['1'] + '  |' + board['2'] + '  |' + board['3'])
    print('--+--+--')
    print(board['4'] + '  |' + board['5'] + '  |' + board['6'])
    print('--+--+--')
    print(board['7'] + '  |' + board['8'] + '  |' + board['9'])

def tic_tac_toe_game():
    count = 0
    player_one_turn = 'X'
    player_two_turn = 'O'
    for i in range(1, 10):
        print_tic_tac_toe_board(Tic_Tac_Toe_Board)
        print("It's your turn " + player_one_turn + ".  Where would you like to move?")
        # Player One will select a place to move.
        move = input()
        
        if move == "":
           print("Invalid move!  Please make a valid selection:")
            continue
        elif int(move) < 1 or int(move) > 9:
          print("Invalid move! Please make a valid selection:")
            continue
             
        if Tic_Tac_Toe_Board[move] == '':
            Tic_Tac_Toe_Board[move] = player_one_turn
            count += 1
        else:
            print("That space is already filled.\n Where would you like to move?")
            continue
            # Starting at turn 3 for player one, the program will check to see if a player has won
            # If one of the players wins, the game is over.
        #     Check across the top
        if count >= 5:
            if Tic_Tac_Toe_Board['1'] == Tic_Tac_Toe_Board['2'] == Tic_Tac_Toe_Board['3'] == player_one_turn:
                print(Tic_Tac_Toe_Board)
                print("Game over!\n")
                print("Player one wins!")
                break

            elif Tic_Tac_Toe_Board['1'] == Tic_Tac_Toe_Board['2'] == Tic_Tac_Toe_Board['3'] == player_two_turn:
                print(Tic_Tac_Toe_Board)
                print("Game over!\n")
                print("Player two wins!")
                break
            #     Check across the middle
            elif Tic_Tac_Toe_Board['4'] == Tic_Tac_Toe_Board['5'] == Tic_Tac_Toe_Board['6'] == player_one_turn:
                print(Tic_Tac_Toe_Board)
                print("Game over!\n")
                print("Player one wins!")
                break

            elif Tic_Tac_Toe_Board['4'] == Tic_Tac_Toe_Board['5'] == Tic_Tac_Toe_Board['6'] == player_two_turn:
                print(Tic_Tac_Toe_Board)
                print("Game over!\n")
                print("Player two wins!")
                break
            #     Check across the bottom
            elif Tic_Tac_Toe_Board['7'] == Tic_Tac_Toe_Board['8'] == Tic_Tac_Toe_Board['9'] == player_one_turn:
                print(Tic_Tac_Toe_Board)
                print("Game over!\n")
                print("Player one wins!")
                break

            elif Tic_Tac_Toe_Board['7'] == Tic_Tac_Toe_Board['8'] == Tic_Tac_Toe_Board['9'] == player_two_turn:
                print(Tic_Tac_Toe_Board)
                print("Game over!\n")
                print("Player two wins!")
                break
#                 Check the left column
            elif Tic_Tac_Toe_Board['1'] == Tic_Tac_Toe_Board['4'] == Tic_Tac_Toe_Board['7'] == player_one_turn:
                print(Tic_Tac_Toe_Board)
                print("Game over!\n")
                print("Player one wins!")
                break

            elif Tic_Tac_Toe_Board['1'] == Tic_Tac_Toe_Board['4'] == Tic_Tac_Toe_Board['7'] == player_two_turn:
                print(Tic_Tac_Toe_Board)
                print("Game over!\n")
                print("Player two wins!")
                break
#                 Check the center column
            elif Tic_Tac_Toe_Board['2'] == Tic_Tac_Toe_Board['5'] == Tic_Tac_Toe_Board['8'] == player_one_turn:
                print(Tic_Tac_Toe_Board)
                print("Game over!\n")
                print("Player one wins!")
                break

            elif Tic_Tac_Toe_Board['2'] == Tic_Tac_Toe_Board['5'] == Tic_Tac_Toe_Board['8'] == player_two_turn:
                print(Tic_Tac_Toe_Board)
                print("Game over!\n")
                print("Player two wins!")
                break
#                 Check the right column
            elif Tic_Tac_Toe_Board['3'] == Tic_Tac_Toe_Board['6'] == Tic_Tac_Toe_Board['9'] == player_one_turn:
                print(Tic_Tac_Toe_Board)
                print("Game over!\n")
                print("Player one wins!")
                break

            elif Tic_Tac_Toe_Board['3'] == Tic_Tac_Toe_Board['6'] == Tic_Tac_Toe_Board['9'] == player_two_turn:
                print(Tic_Tac_Toe_Board)
                print("Game over!\n")
                print("Player two wins!")
                break
            #                 Check the top left to bottom right diagonal
            elif Tic_Tac_Toe_Board['1'] == Tic_Tac_Toe_Board['5'] == Tic_Tac_Toe_Board['9'] == player_one_turn:
                print(Tic_Tac_Toe_Board)
                print("Game over!\n")
                print("Player one wins!")
                break

            elif Tic_Tac_Toe_Board['7'] == Tic_Tac_Toe_Board['8'] == Tic_Tac_Toe_Board['9'] == player_two_turn:
                print(Tic_Tac_Toe_Board)
                print("Game over!\n")
                print("Player two wins!")
                break
#                 Check the bottom left to top right diagonal
            elif Tic_Tac_Toe_Board['7'] == Tic_Tac_Toe_Board['5'] == Tic_Tac_Toe_Board['3'] == player_one_turn:
                print(Tic_Tac_Toe_Board)
                print("Game over!\n")
                print("Player one wins!")
                break

            elif Tic_Tac_Toe_Board['7'] == Tic_Tac_Toe_Board['5'] == Tic_Tac_Toe_Board['3'] == player_two_turn:
                print(Tic_Tac_Toe_Board)
                print("Game over!\n")
                print("Player two wins!")
                break
        # If no player wins and the board is full, the game is declared a tie.
        if count == 9:
            print("Game over!\n")
            print("It is a tie!")
#             Players will alternate turns
        if player_one_turn == 'X':
            player_one_turn = player_two_turn
        else:
            player_one_turn = 'X'

    restart = input("Do you want to play again? (y/n)")
    if restart == 'Y' or restart == 'y':
        for key in ttt_board_keys:
            Tic_Tac_Toe_Board[key] = ''

        tic_tac_toe_game()


if __name__ == "__main__":
    tic_tac_toe_game()









