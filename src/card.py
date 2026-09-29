class Card:
    SUITS = ['♠', '♥', '♦', '♣']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    VALUES = {rank: i for i, rank in enumerate(RANKS, start=2)}

    def __init__(self, rank: str, suit: str):
        if rank not in Card.RANKS or suit not in Card.SUITS:
            raise ValueError(f"Invalid rank ({rank}) or suit ({suit})")
        self.rank = rank
        self.suit = suit
        self.value = Card.VALUES[rank]

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"

    def __repr__(self) -> str:
        return str(self)
