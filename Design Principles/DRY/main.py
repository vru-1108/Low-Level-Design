from member import Member
from loan import Loan
from book_copy import BookCopy
from borrow_exception import BorrowException
from borrowing_service import BorrowingService
from self_checkout_kiosk import SelfCheckoutKiosk
from librarian_service import LibrarianCheckout
def attempt(channel, checkout):
    try:
        print(f"{channel}: {checkout().describe()}")
    except BorrowException as e:
        print(f"{channel} rejected: {e}")


def main():
    borrowing_service = BorrowingService()
    borrowing_service.add_member(Member("M-1", "Alice", True, 0))
    borrowing_service.add_member(Member("M-2", "Bob", False, 0))
    borrowing_service.add_member(Member("M-3", "Carol", True, 5))
    borrowing_service.add_copy(BookCopy("C-1", "The Pragmatic Programmer"))
    borrowing_service.add_copy(BookCopy("C-2", "Clean Code"))

    # Both workflows share the same BorrowingService, so they apply the same rules
    desk = LibrarianCheckout(borrowing_service)
    kiosk = SelfCheckoutKiosk(borrowing_service)

    attempt("Desk", lambda: desk.checkout_at_desk("M-1", "C-1"))
    attempt("Kiosk", lambda: kiosk.checkout_at_kiosk("M-1", "C-1"))
    attempt("Kiosk", lambda: kiosk.checkout_at_kiosk("M-1", "C-2"))
    attempt("Kiosk", lambda: kiosk.checkout_at_kiosk("M-2", "C-2"))
    attempt("Desk", lambda: desk.checkout_at_desk("M-3", "C-1"))


if __name__ == "__main__":
    main()