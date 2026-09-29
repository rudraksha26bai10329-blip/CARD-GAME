import unittest
from src.card import Card

class TestCard(unittest.TestCase):
    def test_card_creation(self):
        card = Card('A', '♠')
        self.assertEqual(card.rank, 'A')
        self.assertEqual(card.suit, '♠')
        self.assertEqual(card.value, 14)

    def test_invalid_card(self):
        with self.assertRaises(ValueError):
            Card('15', '♠')
        with self.assertRaises(ValueError):
            Card('K', 'X')

if __name__ == '__main__':
    unittest.main()
