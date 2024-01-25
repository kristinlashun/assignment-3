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
        if self._fine_amount < 0:
            self._fine_amount = 0  

class Library:
    def __init__(self):
        self._holdings = {}
        self._members = {}
        self._current_date = 0

    def add_library_item(self, item):
        self._holdings[item._library_item_id] = item

    def add_patron(self, patron):
        self._members[patron._patron_id] = patron

    def increment_current_date(self):
        self._current_date += 1
        # Update fines for overdue items for each patron
        for patron_id, patron in self._members.items():
            for item_id in patron._checked_out_items:
                item = self._holdings[item_id]
                if self._current_date - item._date_checked_out > item.get_check_out_length():
                    patron.amend_fine(0.10)  # Assuming 10 cents fine per day overdue

    def pay_fine(self, patron_id, amount):
        patron = self._members.get(patron_id)
        if patron:
            patron.amend_fine(-amount)  # Negative amount to reduce the fine
            return "payment successful"
        else:
            return "patron not found"

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

    # Increment the date, have patron pay fine, check fine amount
    library.increment_current_date()  # This would also need to mark books as overdue and apply fines if needed
    print(patron1._fine_amount)  # Check fine amount before payment
    library.pay_fine("p001", 0.30)  # Patron pays 30 cents fine
    print(patron1._fine_amount)  # Check fine amount after payment

if __name__ == "__main__":
    main()

