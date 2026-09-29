from src.game import CardGameSimulator

if __name__ == "__main__":
    # Initialize and start the game with players
    game = CardGameSimulator(["Alice", "Bob", "Charlie"])
    game.play()
