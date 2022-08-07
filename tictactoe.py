#!/usr/bin/python3
# Automated tic-tac-toe program

from bots import *


def play_game():
    """ Main function to play a game of Tic-tac-toe 
        Changing the class in the players list can
        be the (human) Player, a RandomBot that plays 
        randomly, or a MiniMaxBot or AlphaBetaBot to 
        use the minimax or alpha-beta algorithms.
    """
    print("Game start")
    board = [["-" for i in range(3)] for j in range(3)]
    winner = False
    turn = 0
    players = [AlphaBetaBot("x"), AlphaBetaBot("o")]
    to_move = players[0]

    while (not winner) and turn <= 8:
        play_turn(to_move, board)
        turn += 1
        winner = check_winner(to_move.symbol, board)
        if winner == "draw":
            print("It's a draw!")
        elif winner:
            print(f"\n{winner} wins!")
        if to_move == players[0]:
            to_move = players[1]
        elif to_move == players[1]:
            to_move = players[0]

    print("\n\nFinal Board\n")
    print_board(board)
    print("\n")


def print_board(board):
    for row in board:
        print(row)


def check_winner(to_win, board):
    """ Returns the player that
        won the game, a draw or False if the game is still ongoing"""
    winner = False

    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == to_win:
            winner = row[0]
            break

    # Check columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] == to_win:
            winner = board[0][column]
            break

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == to_win:
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] == to_win:
        winner = board[2][0]

    # Check draws
    if not winner:
        draw = True
        for row in board:
            if "-" in row:
                draw = False
                break
        if draw:
            winner = "draw"

    return winner


def play_turn(to_move, board):
    """Handles updating the board for one single turn in the game"""
    print(f"\n--- {to_move.symbol}'s turn ---")
    print("\n")
    print_board(board)
    valid_choice = False
    while not valid_choice:
        x_choice, y_choice = to_move.get_move(board)
        if 0 <= x_choice <= 2 and 0 <= y_choice <= 2 and board[y_choice][x_choice] == "-":
            valid_choice = True
        else:
            print("invalid choice, try again")

    board[y_choice][x_choice] = to_move.symbol


if __name__ == "__main__":
    play_game()
