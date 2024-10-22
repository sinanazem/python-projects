from src.book import Book
from src.member import StandardMember, PremiumMember
from src.library import Library

def main():
    library = Library("Advanced City Library")
    
    book1 = Book("1984", "George Orwell", "123456789")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "987654321")
    
    member1 = StandardMember("Alice", "M001")
    member2 = PremiumMember("Bob", "M002")
    
    library.add_book(book1)
    library.add_book(book2)
    
    library.add_member(member1)
    library.add_member(member2)
    
    library.check_out_book("123456789", "M001")
    library.reserve_book("123456789", "M002")
    library.return_book("123456789", "M001")
    
    # Premium member checks out the book
    library.check_out_book("123456789", "M002")
    library.return_book("123456789", "M002")

if __name__ == "__main__":
    main()
