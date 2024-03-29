import unittest
from library_member import LibraryMember
from book import Book

class TestLibraryMemberMethods(unittest.TestCase):
    def setUp(self):
        self.member = LibraryMember("Alice", "M001")
        self.book = Book("Python Programming", "John Smith", "978-0134465679", 5)

    def test_borrow_book_available(self):
        # Test borrowing an available book
        self.member.borrow_book(self.book)
        self.assertIn(self.book, self.member.borrowed_books)

    def test_borrow_book_unavailable(self):
        # Test borrowing an unavailable book
        for _ in range(5):  # Exhaust available copies
            self.book.check_out()
        self.member.borrow_book(self.book)
        self.assertNotIn(self.book, self.member.borrowed_books)

    def test_return_book(self):
        # Test returning a book
        self.member.borrow_book(self.book)
        self.member.return_book(self.book)
        self.assertNotIn(self.book, self.member.borrowed_books)

if __name__ == '__main__':
    unittest.main()
