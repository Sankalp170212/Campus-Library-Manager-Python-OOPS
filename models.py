# models.py
"""
Library Management System - Models
Defines LibraryItem (abstract base class), Book, Magazine, DVD, and Member.
"""
from abc import ABC, abstractmethod


class LibraryItem(ABC):
    total_items = 0  # class attribute, shared by every item

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.__available = True          # private attribute
        LibraryItem.total_items += 1     # update the class attribute via the class name

    def is_available(self):
        """Return True if the item is currently available, False otherwise."""
        return self.__available

    def mark_borrowed(self):
        """Mark the item as borrowed (unavailable)."""
        self.__available = False

    def mark_returned(self):
        """Mark the item as returned (available)."""
        self.__available = True

    @abstractmethod
    def late_fee(self, days_late):
        """Calculate the late fee for a given number of days late."""
        pass

    def describe(self):
        """Return a one-line readable description of the item."""
        return f"{self.title} (ID {self.item_id})"


class Book(LibraryItem):
    DAILY_RATE = 2  # Rs 2 per day

    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"Book: {self.title} by {self.author} (ID {self.item_id})"


class Magazine(LibraryItem):
    DAILY_RATE = 1  # Rs 1 per day

    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"Magazine: {self.title} Issue #{self.issue_number} (ID {self.item_id})"


class DVD(LibraryItem):
    DAILY_RATE = 5  # Rs 5 per day

    def __init__(self, title, item_id, duration_minutes):
        super().__init__(title, item_id)
        self.duration_minutes = duration_minutes

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"DVD: {self.title} ({self.duration_minutes} mins) (ID {self.item_id})"


class Member:
    def __init__(self, name, member_id, max_items=3):
        self.name = name
        self.member_id = member_id
        self.max_items = max_items
        self.__borrowed = []  # private list of items

    def borrow(self, item):
        """
        Borrow an item.
        Raises ValueError if the item is not available or if the borrow limit is reached.
        """
        if not item.is_available():
            raise ValueError(f"'{item.title}' is already borrowed.")
        if len(self.__borrowed) >= self.max_items:
            raise ValueError(f"{self.name} has reached the borrowing limit of {self.max_items} item(s).")

        item.mark_borrowed()
        self.__borrowed.append(item)

    def return_item(self, item, days_late=0):
        """
        Return a borrowed item and compute any late fee.
        Raises ValueError if the item was not borrowed by this member.
        """
        if item not in self.__borrowed:
            raise ValueError(f"'{item.title}' is not in {self.name}'s borrowed list.")

        item.mark_returned()
        self.__borrowed.remove(item)
        return item.late_fee(days_late)

    def borrowed_titles(self):
        """Return a list of borrowed item titles without exposing the private __borrowed list."""
        return [item.title for item in self.__borrowed]
