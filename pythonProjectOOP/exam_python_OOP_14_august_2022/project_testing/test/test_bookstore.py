from exam_python_18_april_2022.project import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):

    def setUp(self):
        self.bookstore = Bookstore(10)
        self.books_dict = {"abv": 2, "abc": 1}

    def test_correct_initialization_with_valid_books_limit(self):

        self.assertEqual(10, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_correct_initialization_with_invalid_books_limit(self):

        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -1
        self.assertEqual("Books limit of -1 is not valid", str(ve.exception))

    def test_len_magic_method(self):
        self.bookstore.availability_in_store_by_book_titles = self.books_dict

        self.assertEqual(3, len(self.bookstore))

    def test_receive_book_if_the_limit_for_books_is_passed(self):

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("abc", 11)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_books_in_the_limit(self):

        self.assertEqual("3 copies of abc are available in the bookstore.", self.bookstore.receive_book("abc", 3))
        self.assertEqual({"abc": 3}, self.bookstore.availability_in_store_by_book_titles)

    def test_receive_existing_book_in_the_limit(self):
        self.bookstore.availability_in_store_by_book_titles["abc"] = 2

        self.assertEqual("4 copies of abc are available in the bookstore.", self.bookstore.receive_book("abc", 2))

    def test_sell_book_if_book_is_not_in_the_store(self):

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("abc", 2)

        self.assertEqual("Book abc doesn't exist!", str(ex.exception))

    def test_sell_book_if_not_enough_copies_available(self):
        self.bookstore.availability_in_store_by_book_titles["abc"] = 2

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("abc", 3)

        self.assertEqual("abc has not enough copies to sell. Left: 2", str(ex.exception))

    def test_sell_book_if_name_and_amount_valid(self):
        self.bookstore.availability_in_store_by_book_titles["abc"] = 10
        self.bookstore.availability_in_store_by_book_titles["cba"] = 2

        self.assertEqual("Sold 10 copies of abc", self.bookstore.sell_book("abc", 10))
        self.assertEqual({"abc": 0, "cba": 2}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(10, self.bookstore.total_sold_books)

    def test_str_representation_of_the_class(self):
        self.bookstore.availability_in_store_by_book_titles["abc"] = 3
        self.bookstore.availability_in_store_by_book_titles["cba"] = 2

        self.assertEqual("Total sold books: 0\nCurrent availability: 5\n - abc: 3 copies\n - cba: 2 copies", str(self.bookstore))


if __name__ == '__main__':
    main()

