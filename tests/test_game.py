import unittest
from src.game import CardGameSimulator

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        game = CardGameSimulator(["Alice", "Bob"])
        self.assertEqual(len(game.players), 2)
        self.assertEqual(len(game.deck), 52)

if __name__ == '__main__':
    unittest.main()
