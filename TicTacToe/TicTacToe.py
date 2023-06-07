from json.encoder import INFINITY

# FUNCTIONS

# NAME: Print Board
# ----------
# DESC: Prints the tic-tac-toe board with column and row numbers
# ----------
# ARGS: None
# ----------
# RETURNS: None

def print_board():
    # Print column numbers
    print("  ", end="")
    i = 0
    while i < cols:
        if i != cols - 1:
            print(i + 1, "| ", end="")
        else:
            print(i + 1)
        i += 1

    # Print rows
    i = 0
    while i < rows:
        print(str(i + 1) + " ", end="")
        j = 0
        while j < cols:
            if j == cols - 1:
                print(board[i][j], end="")
            else:
                print(board[i][j], end=" | ")
            j += 1
        print()
        i += 1
    print()

# NAME: Check Win
# ----------
# DESC: Checks the board across, down, and diagonal to determine if there is a winner
# ----------
# ARGS: 
# 1. p (str) - player who just took their turn
# 2. t (int) - turn that just ended
# ----------
# RETURNS: Player who won, draw, or neither

def check_win(p, t):
    # Check across
    r = 0
    while r < rows:
        if board[r][0] == p:
            c = 0
            while c < cols:
                # print("Checking across for", p, "| Row", r + 1, "Col", c + 1, "|", board[r][c])
                if board[r][c] != p:
                    break
                elif c == cols - 1:
                    return p
                c += 1
        r += 1

    # Check down
    c = 0
    while c < cols:
        if board[0][c] == p:
            r = 0
            while r < rows:
                # print("Checking down for", p, "| Row", r + 1, "Col", c + 1, "|", board[r][c])
                if board[r][c] != p:
                    break
                elif r == rows - 1:
                    return p
                r += 1
        c += 1

    # Check diagonal top-left to bottom-right
    r = 0
    c = 0
    if board[0][0] == p:
        while r < rows and c < cols:
            # print("Checking diagonal top-left to bottom-right for", p, "| Row", r + 1, "Col", c + 1, "|", board[r][c])
            if board[r][c] != p:
                break
            elif r == rows - 1 and c == cols - 1:
                return p
            r += 1
            c += 1

    # Check diagonal bottom-left to top-right
    r = rows - 1
    c = 0
    if board[r][0] == p:
        while r > -1 and c < cols:
            # print("Checking diagonal bottom-left to top-right for", p, "| Row", r + 1, "Col", c + 1, "|", board[r][c])
            if board[r][c] != p:
                break
            elif r == 0 and c == cols - 1:
                return p
            r -= 1
            c += 1

    if t == rows*cols:
        return "Draw"

    return None

# NAME: Check Move
# ----------
# DESC: Searches all possible moves following the current move
# ----------
# ARGS: 
# 1. board (2D list) - current game board
# 2. turn (int) - current turn in the game
# 3. depth (int) - current depth of the search
# 4. isMaxPlayer (bool) - if max player (X) just took their move
# ----------
# RETURNS: Best score given the current move

def check_move(board, turn, depth, isMaxPlayer):
    if (isMaxPlayer):
        player = "X"
    else:
        player = "O"

    winner = check_win(player, turn)

    # STATIC EVALUATIONS
    if winner == "O":
        return -1
    elif winner == "Draw":
        return 0
    elif winner == "X":
        return 1

    if isMaxPlayer:
        bestScore = -INFINITY
        i = 0
        while i < rows:
            j = 0
            while j < cols:
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = check_move(board, turn + 1, depth + 1, False)
                    board[i][j] = " "
                    bestScore = max(score, bestScore)
                j += 1
            i += 1
        return bestScore

    else:
        bestScore = INFINITY
        i = 0
        while i < rows:
            j = 0
            while j < cols:
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = check_move(board, turn + 1, depth + 1, True)
                    board[i][j] = " "
                    bestScore = min(score, bestScore)
                j += 1
            i += 1
        return bestScore



print("WELCOME TO TIC-TAC-TOE!")
print("-----------------------")
print()
print("First thing's first, let's set up the board...")
print()

stop = False

while stop == False:
    winner = " "
    player = "X"
    turn = 1
    game_over = False

    rows = 0
    while rows < 3 or rows > 10:
        rows = int(input("Between 3 and 10, how many rows you would like? "))
        if rows < 3:
            print("That's too few rows, try again!")
            print()
        elif rows > 10:
            print("That's too many rows, try again!")
            print()
        else:
            cols = rows
            board = [[" "]*cols for i in range(rows)]

    print()
    print_board()

    while game_over == False:
        if turn%2 == 1:
            player = "X"
        else:
            player = "O"

        turn_complete = False

        while turn_complete == False:
            print("Turn", str(turn) + "!")
            print("Player", player + ", it's your turn!")
            print()
            if player == "O":
                bestScore = INFINITY
                i = 0
                while i < rows:
                    j = 0
                    while j < cols:
                        if board[i][j] == " ":
                            # print("Checking row", i + 1, "column", j + 1)
                            # print_board()
                            board[i][j] = player
                            score = check_move(board, turn, 0, False)
                            board[i][j] = " "
                            if score < bestScore:
                                bestScore = score
                                move_row = i
                                move_col = j
                            # print("Best move is row", move_row + 1, "column", move_col + 1)
                            # print()
                        # else:
                            # print("Row", i + 1, "column", j + 1, "is taken!")
                            # print()
                        j += 1
                    i += 1
                board[move_row][move_col] = player
                print_board()
                winner = check_win(player, turn)
                if winner == player:
                     game_over = True
                     print(player, "is the winner!")
                elif winner == "Draw":
                    game_over = True
                    print("It's a draw!")
                turn += 1
                turn_complete = True
            else:
                input_row = 0
                input_col = 0
                while input_row < 1 or input_row > rows:
                    input_row = int(input("Enter a row: "))
                    if input_row < 1 or input_row > rows:
                        print("That row number's not on the board, try again!")
                        print()
                    else:
                       break
                while input_col < 1 or input_col > cols:
                    input_col = int(input("Enter a column: "))
                    if input_col < 1 or input_col > cols:
                        print("That column number's not on the board, try again!")
                        print()
                    else:
                        break
                input_row = input_row - 1
                input_col = input_col - 1
                print()

                if board[input_row][input_col] == " ":
                    board[input_row][input_col] = player
                    print_board()
                    winner = check_win(player, turn)
                    if winner == player:
                         game_over = True
                         print(player, "is the winner!")
                    elif winner == "Draw":
                        game_over = True
                        print("It's a draw!")
                    turn += 1
                    turn_complete = True
                else:
                    print("That spot's taken, try again!")
    stop_input = input("Would you like to play again? ")
    if stop_input == "n" or stop_input == "N" or stop_input == "no" or stop_input == "No" or stop_input == "NO":
        stop = True