from game import Game
from player import Player
if __name__ == "__main__":
    game = Game(Player("Alice", "X"), Player("Bob", "O"))

    moves = [(1, 1), (0, 0), (0, 0), (0, 2), (0, 1), (2, 0), (2, 1)]
    for r, c in moves:
        player = game.current_player
        if game.make_move(r, c):
            print(f"{player.name} plays ({r}, {c})")
        else:
            print(f"{player.name}'s move ({r}, {c}) is rejected")

    print(game.render())
    print(game.get_result())