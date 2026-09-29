from typing import List
from src.deck import Deck
from src.player import Player

class CardGameSimulator:
    def __init__(self, player_names: List[str]):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]

    def deal_round(self, cards_per_player: int = 1) -> None:
        print(f"\n--- Starting New Round ({len(self.deck)} cards remaining in deck) ---")
        
        for player in self.players:
            player.clear_hand()
            player.receive_cards(self.deck.draw(cards_per_player))
            print(f"{player.name} draws: {player.hand[0]}")

        highest_value = max(p.hand[0].value for p in self.players)
        winners = [p for p in self.players if p.hand[0].value == highest_value]

        if len(winners) > 1:
            print("It's a tie for this round!")
        else:
            winners[0].score += 1
            print(f"🏆 {winners[0].name} wins the round with {winners[0].hand[0]}!")

    def show_scoreboard(self) -> None:
        print("\n--- Current Scores ---")
        for player in self.players:
            print(f"{player.name}: {player.score} pts")

    def play(self) -> None:
        print("Welcome to the High Card Simulator!")
        
        while len(self.deck) >= len(self.players):
            user_input = input("\nPress [Enter] to play next round or type 'q' to quit: ").strip().lower()
            if user_input == 'q':
                break
            
            self.deal_round()
            self.show_scoreboard()

        print("\n=== Game Over ===")
        self.show_scoreboard()
        
        max_score = max(p.score for p in self.players)
        top_players = [p.name for p in self.players if p.score == max_score]
        
        if len(top_players) > 1:
            print(f"\nOverall Game Result: Tie between {', '.join(top_players)}!")
        else:
            print(f"\n🎉 Game Champion: {top_players[0]}! 🎉")
