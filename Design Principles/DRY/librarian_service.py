from borrowing_service import BorrowingService
from loan import Loan
class LibrarianCheckout:
    def __init__(self, borrowing_service: BorrowingService):
        self._borrowing_service = borrowing_service

    def checkout_at_desk(self, member_id: str, copy_id: str) -> Loan:
        return self._borrowing_service.borrow_book(member_id, copy_id)