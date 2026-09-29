import unittest
from src.player import Player
from src.card import Card

class TestPlayer(unittest.TestCase):
    def test_player_receive_and_clear(self):
        player = Player("Alice")
        card = Card('10', '♥')
        player.receive_cards(card)
        self.assertEqual(len(player.hand), 1)
        player.clear_hand()
        self.assertEqual(len(player.hand), 0)

if __name__ == '__main__':
    unittest.main()
