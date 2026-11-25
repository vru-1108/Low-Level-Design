from member import Member
from book_copy import BookCopy

class Loan:
    def __init__(self, member: Member, copy: BookCopy):
        self._member = member
        self._copy = copy

    def describe(self) -> str:
        return f"{self._member.get_name()} borrowed {self._copy.get_copy_id()} ({self._copy.get_title()})"