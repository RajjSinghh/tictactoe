import random
import copy


class Player:
    """Basic class for a human player
       Overriding the get_move() method will allow you to build AI for the game
    """

    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        print("\n")
        x_choice = int(input("Enter the x position of your move: "))
        y_choice = int(input("Enter the y position of your move: "))
        print("\n")
        return [x_choice, y_choice]


class RandomBot(Player):
    """A bot that plays randomly"""

    def __init__(self, symbol):
        super().__init__(symbol)

    def get_legal_moves(self, board):
        legal_moves = []
        for y, row in enumerate(board):
            for x, column in enumerate(row):
                if column == "-":
                    legal_moves.append([x, y])
        return legal_moves

    def get_move(self, board):
        return random.choice(self.get_legal_moves(board))


class MiniMaxBot(Player):
    """ A bot that uses the minimax algorithm to play the game"""
    def __init__(self, symbol):
        super().__init__(symbol)
        # maximizing will be used for minimax algorithm, x is the maximizing
        # player and o is the minimizing player
        if self.symbol == "x":
            self.maximizing = True
        elif self.symbol == "o":
            self.maximizing = False
        else:
            raise ValueError(f"The player must be x or o, not {self.symbol}")

    @staticmethod
    def check_winner(board):
        """Checks the outcome of the game.

           Returns 1 if x wins, -1 if o wins and 0 if it is drawn. None otherwise
        """
        winner = False

        # Check rows
        for row in board:
            if row[0] == row[1] == row[2] and (row[0] != "-"):
                winner = row[0]
                break

        # Column check
        if not winner:
            for column in range(3):
                if board[0][column] == board[1][column] == board[2][column] and (board[0][column] != "-"):
                    winner = board[0][column]
                    break

        # Diagonal check
        if not winner:
            if board[0][0] == board[1][1] == board[2][2] and (board[0][0] != "-"):
                winner = board[0][0]
            elif board[0][2] == board[1][1] == board[2][0] and (board[0][2] != "-"):
                winner = board[0][2]

        # Check for draws
        if not winner:
            draw = True
            for row in board:
                if "-" in row:
                    draw = False
                    break

        if winner == "x":
            return 1
        elif winner == "o":
            return -1
        elif draw:
            return 0
        else:
            return None

    def get_legal_moves(self, board):
        """Returns the legal moves (empty cells) of the board"""
        legal_moves = []
        for y, row in enumerate(board):
            for x, column in enumerate(row):
                if column == "-":
                    legal_moves.append([x, y])
        return legal_moves

    def evaluate(self, board, maximizing):
        """Minimax algorithm used to evaluate a given position"""
        # Base cae
        if MiniMaxBot.check_winner(board) != None:
            return MiniMaxBot.check_winner(board)

        # Recursive step
        if maximizing:
            value = -1 * float("inf")
            for x, y in self.get_legal_moves(board):
                board[y][x] = "x"
                value = max(value, self.evaluate(board, False))
                board[y][x] = "-"
            return value

        else:  # Minimizing player
            value = float("inf")
            for x, y in self.get_legal_moves(board):
                board[y][x] = "o"
                value = min(value, self.evaluate(board, True))
                board[y][x] = "-"
            return value

    def get_move(self, board):
        legal_moves = self.get_legal_moves(board)
        best_move = None
        if self.maximizing:
            evaluation = -1 * float("inf")
        else:
            evaluation = float("inf")

        for x, y in legal_moves:
            board[y][x] = self.symbol
            e = self.evaluate(board, not self.maximizing)
            if (self.maximizing) and (e > evaluation):
                evaluation = e
                best_move = [x, y]
            elif (not self.maximizing) and (e < evaluation):
                evaluation = e
                best_move = [x, y]
            board[y][x] = "-"

        return best_move

class AlphaBetaBot(MiniMaxBot):
    """ A bot that uses the alpha-beta pruning algorithm to play the game"""
    def __init__(self, symbol):
        super().__init__(symbol)

    def evaluate(self, board, alpha, beta, maximizing):
        """Alpha Beta pruning algorithm algorithm used to evaluate a given position"""
        # Base cae
        if MiniMaxBot.check_winner(board) != None:
            return MiniMaxBot.check_winner(board)

        # Recursive step
        if maximizing:
            value = -1 * float("inf")
            for x, y in self.get_legal_moves(board):
                board[y][x] = "x"
                value = max(value, self.evaluate(board, alpha, beta, False))
                board[y][x] = "-"
                if value >= beta:
                    break
                alpha = max(alpha, value)
            return value

        else:  # Minimizing player
            value = float("inf")
            for x, y in self.get_legal_moves(board):
                board[y][x] = "o"
                value = min(value, self.evaluate(board, alpha, beta, True))
                board[y][x] = "-"
                if value <= alpha:
                    break
                beta = min(beta, value)
            return value

    def get_move(self, board):
        legal_moves = self.get_legal_moves(board)
        best_move = None
        if self.maximizing:
            evaluation = -1 * float("inf")
        else:
            evaluation = float("inf")

        for x, y in legal_moves:
            board[y][x] = self.symbol
            e = self.evaluate(board, -1 * float("inf"), float("inf"), not self.maximizing)
            if (self.maximizing) and (e > evaluation):
                evaluation = e
                best_move = [x, y]
            elif (not self.maximizing) and (e < evaluation):
                evaluation = e
                best_move = [x, y]
            board[y][x] = "-"

        return best_move

