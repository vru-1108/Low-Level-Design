class Member:
    def __init__(self, member_id: str, name: str, active: bool, active_loans: int):
        self._member_id = member_id
        self._name = name
        self._active = active
        self._active_loans = active_loans

    def get_member_id(self) -> str:
        return self._member_id

    def get_name(self) -> str:
        return self._name

    def is_active(self) -> bool:
        return self._active

    def active_loans(self) -> int:
        return self._active_loans

    def record_loan(self) -> None:
        self._active_loans += 1