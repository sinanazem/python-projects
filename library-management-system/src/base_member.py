from abc import ABC, abstractmethod

class BaseMember(ABC):
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self._borrowed_books = []  # Protected attribute to allow subclasses to access
        self._borrow_limit = 0     # Borrow limit to be defined by subclasses

    @abstractmethod
    def borrow_book(self, book):
        pass

    @abstractmethod
    def return_book(self, book):
        pass

    def __str__(self):
        return f"Member(name='{self.name}', member_id='{self.member_id}')"

    def __repr__(self):
        return f"Member(name={self.name!r}, member_id={self.member_id!r})"

    def __eq__(self, other):
        if isinstance(other, BaseMember):
            return self.member_id == other.member_id
        return False

    def _can_borrow(self):
        return len(self._borrowed_books) < self._borrow_limit
