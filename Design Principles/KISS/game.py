from player import Player
from board import Board
class Game:
    def __init__(self, first: Player, second: Player):
        self._board = Board()
        self._players = [first, second]
        self._current = 0
        self._game_over = False
        self._winner: Player | None = None

    @property
    def current_player(self) -> Player:
        return self._players[self._current]

    def make_move(self, r: int, c: int) -> bool:
        if not self._is_valid(r, c):
            return False
        player = self._players[self._current]
        self._board.place_symbol(r, c, player.symbol)
        if self._check_win(player.symbol):
            self._winner = player
            self._game_over = True
        elif self._board.is_full():
            self._game_over = True
        else:
            self._switch_turn()
        return True

    def get_result(self) -> str:
        if self._winner is not None:
            return f"{self._winner.name} ({self._winner.symbol}) wins"
        return "Draw" if self._game_over else "In progress"

    def render(self) -> str:
        return self._board.render()

    def _is_valid(self, r: int, c: int) -> bool:
        if self._game_over:
            return False
        if r < 0 or r > 2 or c < 0 or c > 2:
            return False
        return self._board.is_empty(r, c)

    def _check_win(self, s: str) -> bool:
        for i in range(3):
            if self._line(s, i, 0, i, 1, i, 2):
                return True
            if self._line(s, 0, i, 1, i, 2, i):
                return True
        return self._line(s, 0, 0, 1, 1, 2, 2) or self._line(s, 0, 2, 1, 1, 2, 0)

    def _line(self, s: str, r1: int, c1: int, r2: int, c2: int, r3: int, c3: int) -> bool:
        return (self._board.get_symbol(r1, c1) == s
                and self._board.get_symbol(r2, c2) == s
                and self._board.get_symbol(r3, c3) == s)

    def _switch_turn(self) -> None:
        self._current = 1 - self._current