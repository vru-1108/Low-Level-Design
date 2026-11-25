class BookCopy:
    def __init__(self, copy_id: str, title: str):
        self._copy_id = copy_id
        self._title = title
        self._available = True

    def get_copy_id(self) -> str:
        return self._copy_id

    def get_title(self) -> str:
        return self._title

    def is_available(self) -> bool:
        return self._available

    def mark_borrowed(self) -> None:
        self._available = False