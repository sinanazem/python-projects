from base_member import BaseMember

class StandardMember(BaseMember):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self._borrow_limit = 3

    def borrow_book(self, book):
        if self._can_borrow() and book.is_available():
            book.check_out()
            self._borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        elif not self._can_borrow():
            print(f"{self.name} has reached the borrow limit.")
        else:
            print(f"{book.title} is unavailable for borrowing.")

    def return_book(self, book):
        if book in self._borrowed_books:
            book.return_book()
            self._borrowed_books.remove(book)
            print(f"{book.title} returned by {self.name}")
        else:
            print(f"{book.title} cannot be returned by {self.name}; it wasn't borrowed.")

class PremiumMember(BaseMember):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self._borrow_limit = 5

    def borrow_book(self, book):
        if self._can_borrow() and book.is_available():
            book.check_out()
            self._borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}' [Premium]")
        elif not self._can_borrow():
            print(f"{self.name} has reached the borrow limit.")
        else:
            print(f"{book.title} is unavailable for borrowing.")

    def return_book(self, book):
        if book in self._borrowed_books:
            book.return_book()
            self._borrowed_books.remove(book)
            print(f"{book.title} returned by {self.name}")
        else:
            print(f"{book.title} cannot be returned by {self.name}; it wasn't borrowed.")
