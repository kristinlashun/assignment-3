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

    def get_author(self):
        return self._author

    def get_check_out_length(self):
        return 21

class Album(LibraryItem):
    def __init__(self, library_item_id, title, artist):
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        return self._artist

    def get_check_out_length(self):
        return 14

class Movie(LibraryItem):
    def __init__(self, library_item_id, title, director):
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        return self._director

    def get_check_out_length(self):
        return 7

class Patron:
    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0.0

class Library:
    def __init__(self):
        self._holdings = {}
        self._members = {}
        self._current_date = 0

def main():
    b1 = Book("345", "Phantom Tollbooth", "Juster")
    a1 = Album("456", "...And His Orchestra", "The Fastbacks")
    m1 = Movie("567", "Laputa", "Miyazaki")

    p1 = Patron("abc", "Felicity")
    p2 = Patron("bcd", "Waldo")

    lib = Library()
    lib.add_library_item(b1)
    lib.add_library_item(a1)
    lib.add_library_item(m1)
    lib.add_patron(p1)
    lib.add_patron(p2)

if __name__ == "__main__":
    main()
