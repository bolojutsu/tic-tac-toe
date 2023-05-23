def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


def check_win(board, player):
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def get_move(board, player):
    valid_move = False
    while not valid_move:
        move = input(f"Player {player}, enter a move (0-8): ")
        if move.isdigit() and int(move) >= 0 and int(move) <= 8 and board[int(move)] == "":
            return int(move)
        else:
            print("Invalid move. Try again.")


def tic_tac_toe():
    board = [""] * 9
    players = ["X", "O"]
    current_player = 0
    while "" in board and not check_win(board, players[current_player]):
        print_board(board)
        move = get_move(board, players[current_player])
        board[move] = players[current_player]
        current_player = (current_player + 1) % 2
    print_board(board)
    if check_win(board, players[current_player]):
        print(f"Player {players[current_player]} wins!")
    else:
        print("Tie game.")


tic_tac_toe()




