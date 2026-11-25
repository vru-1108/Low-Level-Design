from member import Member
from loan import Loan
from book_copy import BookCopy
from borrow_exception import BorrowException
class BorrowingService:
    # The borrowing limit lives in exactly one place
    MAX_LOANS = 5

    def __init__(self):
        self._members: dict[str, Member] = {}
        self._copies: dict[str, BookCopy] = {}
        self._loans: list[Loan] = []

    def add_member(self, member: Member) -> None:
        self._members[member.get_member_id()] = member

    def add_copy(self, copy: BookCopy) -> None:
        self._copies[copy.get_copy_id()] = copy

    def borrow_book(self, member_id: str, copy_id: str) -> Loan:
        member = self._members[member_id]
        copy = self._copies[copy_id]
        if not member.is_active():
            raise BorrowException("inactive")
        if member.active_loans() >= self.MAX_LOANS:
            raise BorrowException("limit reached")
        if not copy.is_available():
            raise BorrowException("not available")
        loan = Loan(member, copy)
        self._loans.append(loan)
        member.record_loan()
        copy.mark_borrowed()
        return loan