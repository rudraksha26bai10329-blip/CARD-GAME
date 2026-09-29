import unittest
from src.deck import Deck

class TestDeck(unittest.TestCase):
    def test_deck_initialization(self):
        deck = Deck()
        self.assertEqual(len(deck), 52)

    def test_draw_card(self):
        deck = Deck()
        card = deck.draw(1)
        self.assertEqual(len(deck), 51)

    def test_draw_over_limit(self):
        deck = Deck()
        with self.assertRaises(ValueError):
            deck.draw(53)

if __name__ == '__main__':
    unittest.main()
