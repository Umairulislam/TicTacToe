# Global Variables

# Create board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-", ]
# If game is still going
gameStillGoing = True
# Win or Tie
winner = None
# Who's turn
currentPlayer = "X"

# display board


def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def playGame():
    # display initial board
    displayBoard()

    while gameStillGoing:
        handleTurn(currentPlayer)
        checkIfGameOver()
        flipPlayer()
    # When the game ended
    if winner == "X" or winner == "O":
        print(winner + " Wins :D")
    elif winner == None:
        print("Tie :(")

# handle a single turn of an arbitrary player


def handleTurn(player):
    print(player + "'s Turn.")
    position = input("Choose a position from 1 to 9: ")

    # if position aready filled you can't go there
    valid = False
    while not valid:
        # if position not in range then ask again
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1 to 9: ")
        # start position from 1
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there \nEnter the position again")

    board[position] = player
    displayBoard()


def checkIfGameOver():
    checkForWinner()
    checkIfTie()


def checkForWinner():
    global winner
    # Check rows
    rowWinner = checkRows()
    # Check columns
    colsWinner = checkCols()
    # Check diagnolas
    diagsWinner = checkDiags()
    if rowWinner:
        winner = rowWinner
    elif colsWinner:
        winner = colsWinner
    elif diagsWinner:
        winner = diagsWinner
    else:
        winner = None
    return


def checkRows():
    # Global variable
    global gameStillGoing
    # Check if any row has the same value
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    # if any row matches
    if row1 or row2 or row3:
        gameStillGoing = False
    # Return winner 'X' or 'O'
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    return


def checkCols():
    # Global variable
    global gameStillGoing
    # Check if any column has the same value
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    # if any column matches
    if col1 or col2 or col3:
        gameStillGoing = False
    # Return winner 'X' or 'O'
    if col1:
        return board[0]
    if col2:
        return board[1]
    if col3:
        return board[2]
    return


def checkDiags():
    # Global variable
    global gameStillGoing
    # Check if any diagonal has the same value
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"
    # if any diagonal matches
    if diag1 or diag2:
        gameStillGoing = False
    # Return winner 'X' or 'O'
    if diag1:
        return board[0]
    if diag2:
        return board[2]
    return


def checkIfTie():
    # Global varibale
    global gameStillGoing
    if "-" not in board:
        gameStillGoing = False
    return


def flipPlayer():
    # Global variable
    global currentPlayer
    # Switch player
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"
    return


playGame()


# board
# play game
# handle return
# check win
#   check cols
#   check rows
#   check diags
# check tie
# flip player
