from src.book import Book
from src.member import StandardMember, PremiumMember

class Library:
    def __init__(self, name):
        self.name = name
        self.__books = {}
        self.__members = {}

    def add_book(self, book: Book):
        if book.isbn not in self.__books:
            self.__books[book.isbn] = book
            print(f"Book '{book.title}' added to the library.")
        else:
            print(f"Book '{book.title}' is already in the library.")

    def add_member(self, member: StandardMember):
        if member.member_id not in self.__members:
            self.__members[member.member_id] = member
            print(f"Member '{member.name}' added to the library.")
        else:
            print(f"Member '{member.name}' is already registered.")

    def check_out_book(self, isbn: str, member_id: str):
        member = self.__members.get(member_id)
        book = self.__books.get(isbn)
        if member and book:
            member.borrow_book(book)
        elif not member:
            print("Member not found.")
        else:
            print("Book not found.")

    def return_book(self, isbn: str, member_id: str):
        member = self.__members.get(member_id)
        book = self.__books.get(isbn)
        if member and book:
            member.return_book(book)
        elif not member:
            print("Member not found.")
        else:
            print("Book not found.")

    def reserve_book(self, isbn: str, member_id: str):
        member = self.__members.get(member_id)
        book = self.__books.get(isbn)
        if member and book:
            book.reserve(member)
        elif not member:
            print("Member not found.")
        else:
            print("Book not found.")

    def cancel_reservation(self, isbn: str, member_id: str):
        member = self.__members.get(member_id)
        book = self.__books.get(isbn)
        if member and book and book.is_reserved_by(member):
            book.cancel_reservation(member)
        elif not member:
            print("Member not found.")
        else:
            print("Reservation not found or wrong member.")
            


    @property
    def books(self):
        return self.__books

    @property
    def members(self):
        return self.__members

    def __str__(self):
        return f"Library(name='{self.name}')"

    def __repr__(self):
        return f"Library(name={self.name!r})"
