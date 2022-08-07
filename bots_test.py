import unittest
from bots import *


class MiniMaxBotTest(unittest.TestCase):
    def test_check_winner(self):
        board = [
            ["x", "x", "x"],
            ["-", "o", "o"],
            ["-", "-", "-"]
        ]

        self.assertEqual(MiniMaxBot.check_winner(board), 1)

        board = [
            ["o", "o", "o"],
            ["-", "x", "x"],
            ["-", "-", "-"]
        ]

        self.assertEqual(MiniMaxBot.check_winner(board), -1)

        board = [
            ["-", "o", "o"],
            ["-", "x", "x"],
            ["-", "-", "-"]
        ]

        self.assertEqual(MiniMaxBot.check_winner(board), None)

        board = [
            ["o", "x", "o"],
            ["o", "x", "x"],
            ["x", "o", "x"]
        ]

        self.assertEqual(MiniMaxBot.check_winner(board), 0)

        board = [
            ["x", "x", "x"],
            ["-", "o", "o"],
            ["o", "x", "o"]
        ]

        self.assertEqual(MiniMaxBot.check_winner(board), 1)

        board = [
            ["o", "x", "x"],
            ["x", "o", "o"],
            ["o", "x", "o"]
        ]

        self.assertEqual(MiniMaxBot.check_winner(board), -1)

    def test_evaluation(self):
        x = MiniMaxBot("x")
        o = MiniMaxBot("o")

        # Recursive base cases
        board = [
            ["x", "x", "x"],
            ["o", "o", "-"],
            ["-", "-", "-"]
        ]

        self.assertEqual(x.evaluate(board, x.maximizing), 1)
        self.assertEqual(o.evaluate(board, o.maximizing), 1)

        board = [
            ["o", "o", "o"],
            ["x", "x", "-"],
            ["-", "-", "-"]
        ]

        self.assertEqual(x.evaluate(board, x.maximizing), -1)
        self.assertEqual(o.evaluate(board, o.maximizing), -1)

        board = [
            ["o", "x", "o"],
            ["o", "x", "x"],
            ["x", "o", "x"]
        ]

        self.assertEqual(x.evaluate(board, x.maximizing), 0)
        self.assertEqual(o.evaluate(board, o.maximizing), 0)

        # Testing recursive case

        board = [
            ["-", "x", "o"],
            ["o", "x", "x"],
            ["x", "o", "x"]
        ]

        self.assertEqual(x.evaluate(board, x.maximizing), 1)
        self.assertEqual(o.evaluate(board, o.maximizing), 0)

        board = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]

        self.assertEqual(x.evaluate(board, x.maximizing), 0)
        self.assertEqual(o.evaluate(board, o.maximizing), 0)


if __name__ == "__main__":
    unittest.main()
