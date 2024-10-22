# Library Management System Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [System Architecture](#system-architecture)
3. [Class Descriptions](#class-descriptions)
4. [Usage Examples](#usage-examples)
5. [Installation and Setup](#installation-and-setup)
6. [Future Enhancements](#future-enhancements)
7. [Conclusion](#conclusion)

---

## Introduction

### Purpose

The Library Management System is designed to automate the process of managing the lending and returning of books in a library. It streamlines operations for the library staff and provides tools for managing book reservations, member borrowing privileges, and more.

### Scope

- Manage library books and members.
- Support different member types with varying borrowing privileges.
- Track the status of book availability and reservations.
- Provide basic notification mechanisms for administration tasks.

---

## System Architecture

### Overview

The system is implemented using Python with an object-oriented design. It utilizes principles of encapsulation, inheritance, and abstraction to ensure modularity and scalability.


- **Modules**: The system is organized into several Python modules, each handling specific aspects of the project:
  - `book.py`: Manages book details and status.
  - `base_member.py`: Abstract base class for library members.
  - `member.py`: Concrete member classes implementing borrowing logic.
  - `library.py`: Manages collections of books and members.
  - `main.py`: Entry point for program execution.


---

## Class Descriptions

### `Book`

- **Attributes**: `title`, `author`, `isbn`, `__available`, `__reserved_by`.
- **Methods**:
  - `is_available()`: Returns the availability status.
  - `reserve(member)`: Manages reservation by members.
  - `cancel_reservation(member)`: Cancels reservations.
  - `check_out()`: Marks book as checked out.
  - `return_book()`: Marks book as returned.
  - `is_reserved_by(member)`: Checks if reserved by a member.

### `BaseMember` (Abstract Class)

- **Attributes**: `name`, `member_id`, `_borrowed_books`, `_borrow_limit`.
- **Abstract Methods**:
  - `borrow_book(book)`: Borrow a book (implemented by subclasses).
  - `return_book(book)`: Return a book (implemented by subclasses).
- **Methods**:
  - `_can_borrow()`: Private method to check borrow limits.
  - `__str__()` and `__repr__()`: String representations.

### `StandardMember` and `PremiumMember`

- **Inherits**: `BaseMember`
- **Attributes**:
  - `StandardMember` has a borrow limit of 3.
  - `PremiumMember` has a borrow limit of 5.
- **Methods**:
  - `borrow_book(book)`: Overrides abstract method, with specific limits.
  - `return_book(book)`: Handles book returns for members.

### `Library`

- **Attributes**: `name`, `__books`, `__members`.
- **Methods**:
  - `add_book(book)`: Adds a book to the collection.
  - `add_member(member)`: Registers a new member.
  - `check_out_book(isbn, member_id)`: Manages book checkouts.
  - `return_book(isbn, member_id)`: Manages book returns.
  - `reserve_book(isbn, member_id)`: Handles reservations.
  - `cancel_reservation(isbn, member_id)`: Cancels reservations.

---

## Usage Examples

Here is a basic usage scenario demonstrating how to interact with the system:

```python
# Create a library instance
library = Library("Advanced City Library")

# Add books
book1 = Book("1984", "George Orwell", "123456789")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "987654321")
library.add_book(book1)
library.add_book(book2)

# Add members
member1 = StandardMember("Alice", "M001")
member2 = PremiumMember("Bob", "M002")
library.add_member(member1)
library.add_member(member2)

# Member interactions
library.check_out_book("123456789", "M001")
library.reserve_book("123456789", "M002")
library.return_book("123456789", "M001")
library.check_out_book("123456789", "M002")
library.return_book("123456789", "M002")
```

---

## Installation and Setup

1. **Pre-requisites**:
   - Python 3.x installed on your system.
   - Basic understanding of OOP in Python.

2. **Steps**:
   - Clone the repository or download the project files.
   - Navigate to the project directory.
   - Run the main application using `python main.py`.

---

## Future Enhancements

- **Graphical User Interface (GUI)**: Implement a user-friendly GUI for library staff and members.
- **Notification System**: Email or messaging service to notify members about overdue books or available reservations.
- **Database Integration**: Persistence using a database system to store books and member records.

---

## Conclusion

This Library Management System project provides a robust framework for managing library operations. It showcases object-oriented programming techniques, including encapsulation, inheritance, abstraction, and modular design in Python. The system can be extended and integrated with other technologies for enhanced functionality.

--- 

This document covers the essential aspects of the project, including its structure, class functionality, usage, and potential areas for future growth. Adjustments can be made based on specific project requirements or audience needs.