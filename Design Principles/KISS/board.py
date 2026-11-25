class Board:
    EMPTY = "."

    def __init__(self):
        self._cells = [[Board.EMPTY] * 3 for _ in range(3)]

    def is_empty(self, r: int, c: int) -> bool:
        return self._cells[r][c] == Board.EMPTY

    def place_symbol(self, r: int, c: int, s: str) -> None:
        self._cells[r][c] = s

    def get_symbol(self, r: int, c: int) -> str:
        return self._cells[r][c]

    def is_full(self) -> bool:
        return all(cell != Board.EMPTY for row in self._cells for cell in row)

    def render(self) -> str:
        return "\n".join(" ".join(row) for row in self._cells)