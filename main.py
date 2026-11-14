
from models import LibraryItem, Book, Magazine, DVD, Member


def main():
    print("LIBRARY MANAGEMENT SYSTEM")

    print("\n[CHECKPOINT 1] Testing Abstract Class")
    try:
        item = LibraryItem("x", 1)
    except TypeError as e:
        print("Cannot create LibraryItem:", e)

    # Create library items
    book = Book("Python 101", 1, "A. Rao")
    magazine = Magazine("Tech Monthly", 2, 42)
    dvd = DVD("Inception", 3, 148)

    # Create members
    alice = Member("Alice", 101)
    bob = Member("Bob", 102, max_items=1)

    print("\n[CHECKPOINT 2] Testing Borrowing and Error Handling")
    try:
        alice.borrow(book)
        print("Alice borrowed:", book.describe())
        bob.borrow(book)
    except ValueError as e:
        print("Could not borrow:", e)

    print("\n[CHECKPOINT 3] Testing Borrow Limit")
    try:
        bob.borrow(magazine)
        print("Bob borrowed:", magazine.describe())
        bob.borrow(dvd)
    except ValueError as e:
        print("Could not borrow:", e)

    print("\n[CHECKPOINT 4] Testing Return Error")
    try:
        alice.return_item(dvd)
    except ValueError as e:
        print("Could not return:", e)

    print("\n[CHECKPOINT 5] Testing Successful Return and Late Fee")
    fee = alice.return_item(book, days_late=2)
    print("Alice returned:", book.title)
    print("Late fee: Rs", fee)

    print("\n[CHECKPOINT 6] Testing Alice's Borrowing Limit")
    try:
        alice.borrow(book)
        alice.borrow(dvd)

        extra_book = Book("Clean Code", 4, "R. Martin")
        alice.borrow(extra_book)

        print("Alice borrowed:", alice.borrowed_titles())

        fourth_item = Book("Design Patterns", 5, "GoF")
        alice.borrow(fourth_item)

    except ValueError as e:
        print("Could not borrow:", e)

    print("\n[CHECKPOINT 7] Testing Polymorphism")
    items = [book, magazine, dvd]

    for item in items:
        fee = item.late_fee(3)
        print(item.describe(), "-> Late fee: Rs", fee)

    print("\n[CHECKPOINT 8] Testing Class Attribute")
    print("Total items:", LibraryItem.total_items)
    print("Total books:", Book.total_items)

    print("\n[CHECKPOINT 9] Testing Encapsulation")
    try:
        print(book.__available)
    except AttributeError:
        print("Cannot access private availability directly")

    print("Book availability:", book.is_available())

    try:
        print(alice.__borrowed)
    except AttributeError:
        print("Cannot access private borrowed list directly")

    print("Borrowed books:", alice.borrowed_titles())

    print("\nAll checkpoints completed.")


if __name__ == "__main__":
    main()
