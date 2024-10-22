class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True
        self.__reserved_by = None

    def is_available(self):
        return self.__available

    def reserve(self, member):
        if not self.__available and self.__reserved_by is None:
            self.__reserved_by = member
            print(f"Book '{self.title}' reserved by {member.name}.")
        elif self.__reserved_by == member:
            print(f"Book '{self.title}' is already reserved by you.")
        else:
            if self.__available:
                print(f"Book '{self.title}' is available; please check it out.")
            else:
                print(f"Book '{self.title}' is already reserved.")

    def cancel_reservation(self, member):
        if self.__reserved_by == member:
            self.__reserved_by = None
            print(f"Reservation for book '{self.title}' by {member.name} cancelled.")

    def check_out(self):
        if self.__available:
            self.__available = False
            print(f"Book '{self.title}' has been checked out.")
        else:
            print(f"Book '{self.title}' is unavailable.")

    def return_book(self):
        if not self.__available:
            self.__available = True
            self.__reserved_by = None
            print(f"Book '{self.title}' has been returned.")
        else:
            print(f"Book '{self.title}' was not checked out.")

    def is_reserved_by(self, member):
        return self.__reserved_by == member

    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, isbn={self.isbn!r})"
