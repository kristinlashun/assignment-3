# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: 1/24/2024

"""
Description:
This file contains the classes LibraryItem, Book, Album, Movie, Patron, and Library to simulate a library system.
Library items can be checked out, requested, and returned. Patrons can check out items, request items, accrue fines, and make payments.
The Library class manages the operations, including adding items and patrons, checking out and returning items, handling requests,
processing payments, and updating fines.
"""

# Library.py

class LibraryItem:
    def __init__(self, library_item_id, title):
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

class Book(LibraryItem):
    def __init__(self, library_item_id, title, author):
        super().__init__(library_item_id, title)
        self._author = author

    def get_check_out_length(self):
        return 21

class Album(LibraryItem):
    def __init__(self, library_item_id, title, artist):
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_check_out_length(self):
        return 14

class Movie(LibraryItem):
    def __init__(self, library_item_id, title, director):
        super().__init__(library_item_id, title)
        self._director = director

    def get_check_out_length(self):
        return 7

class Patron:
    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0.0

    def amend_fine(self, amount):
        self._fine_amount += amount

class Library:
    def __init__(self):
        self._holdings = {}
        self._members = {}
        self._current_date = 0

    def add_library_item(self, item):
        self._holdings[item._library_item_id] = item

    def add_patron(self, patron):
        self._members[patron._patron_id] = patron

    def check_out_library_item(self, patron_id, library_item_id):
        patron = self._members.get(patron_id)
        if not patron:
            return "patron not found"
        
        item = self._holdings.get(library_item_id)
        if not item:
            return "item not found"
        
        if item._location == "CHECKED_OUT":
            return "item already checked out"
        
        if item._requested_by and item._requested_by != patron_id:
            return "item on hold by other patron"
        
        item._location = "CHECKED_OUT"
        item._checked_out_by = patron_id
        item._date_checked_out = self._current_date
        patron._checked_out_items.append(item._library_item_id)
        
        return "check out successful"

    def increment_current_date(self):
        self._current_date += 1
        for patron in self._members.values():
            for item_id in patron._checked_out_items:
                item = self._holdings[item_id]
                overdue_days = self._current_date - item._date_checked_out - item.get_check_out_length()
                if overdue_days > 0:
                    patron.amend_fine(overdue_days * 0.10)

    def pay_fine(self, patron_id, amount):
        patron = self._members.get(patron_id)
        if patron:
            patron.amend_fine(-amount)
            return "payment successful"
        return "patron not found"

# Main function for demonstration and testing
def main():
    # Create two books
    book1 = Book("001", "Book One", "Author A")
    book2 = Book("002", "Book Two", "Author B")

    # Create two patrons
    patron1 = Patron("p001", "Patron One")
    patron2 = Patron("p002", "Patron Two")

    # Create a library and add books and patrons
    library = Library()
    library.add_library_item(book1)
    library.add_library_item(book2)
    library.add_patron(patron1)
    library.add_patron(patron2)

    # Perform library operations
    library.check_out_library_item("p001", "001")
    library.increment_current_date()  # Days pass
    fine_before_payment = patron1._fine_amount
    library.pay_fine("p001", fine_before_payment)
    fine_after_payment = patron1._fine_amount

if __name__ == "__main__":
    main()
