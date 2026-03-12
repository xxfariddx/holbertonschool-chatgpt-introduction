#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # input loop for valid row
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                if row < 0 or row > 2:
                    print("Row must be 0, 1, or 2.")
                    continue
                break
            except ValueError:
                print("Invalid input. Enter a number between 0 and 2.")

        # input loop for valid column
        while True:
            try:
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if col < 0 or col > 2:
                    print("Column must be 0, 1, or 2.")
                    continue
                break
            except ValueError:
                print("Invalid input. Enter a number between 0 and 2.")

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # check for tie
        if all(cell != " " for row_cells in board for cell in row_cells):
            print_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()