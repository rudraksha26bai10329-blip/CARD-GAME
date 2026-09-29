from typing import Union, List
from src.card import Card

class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand: List[Card] = []
        self.score: int = 0

    def receive_cards(self, cards: Union[Card, List[Card]]) -> None:
        if isinstance(cards, list):
            self.hand.extend(cards)
        else:
            self.hand.append(cards)

    def show_hand(self) -> str:
        hand_str = ", ".join([str(card) for card in self.hand])
        return f"{self.name}'s Hand: [{hand_str}]"

    def clear_hand(self) -> None:
        self.hand = []
