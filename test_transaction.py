import unittest
from transaction import Transaction
from library_member import LibraryMember
from book import Book

""" This will test the process of borrowing book through Transaction class"""

class TestTransactionMethods(unittest.TestCase):
    def setUp(self):
        self.member = LibraryMember("Alice", "M001")
        self.book = Book("Python Programming", "John Smith", "978-0134465679", 5)

    def test_process_transaction_success(self):
        # Test successful transaction
        transaction = Transaction(self.book, self.member)
        transaction.process_transaction()
        self.assertIn(self.book, self.member.borrowed_books)

    def test_process_transaction_unavailable_book(self):
        # Test transaction with an unavailable book
        for _ in range(5):  # Exhaust available copies
            self.book.check_out()
        transaction = Transaction(self.book, self.member)
        transaction.process_transaction()
        self.assertNotIn(self.book, self.member.borrowed_books)

if __name__ == '__main__':
    unittest.main()
