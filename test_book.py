import unittest
from book import Book

class TestBookMethods(unittest.TestCase):
    def setUp(self):
        self.book = Book("Python Programming", "John Smith", "978-0134465679", 5)

    def test_check_out_available_book(self):
        # Test checking out an available book
        self.assertTrue(self.book.check_out())

    def test_check_out_unavailable_book(self):
        # Test checking out an unavailable book
        for _ in range(5):  # Exhaust available copies
            self.book.check_out()
        self.assertFalse(self.book.check_out())

    def test_return_book(self):
        # Test returning a book
        self.book.check_out()
        self.book.return_book()
        self.assertEqual(self.book.available_copies, 5)  # Check if available copies are restored

if __name__ == '__main__':
    unittest.main()