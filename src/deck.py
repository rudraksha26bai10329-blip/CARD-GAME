import random
from typing import Union, List
from src.card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
        self.shuffle()

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self, count: int = 1) -> Union[Card, List[Card]]:
        if count > len(self.cards):
            raise ValueError("Not enough cards remaining in the deck.")
        drawn_cards = [self.cards.pop() for _ in range(count)]
        return drawn_cards[0] if count == 1 else drawn_cards

    def __len__(self) -> int:
        return len(self.cards)
