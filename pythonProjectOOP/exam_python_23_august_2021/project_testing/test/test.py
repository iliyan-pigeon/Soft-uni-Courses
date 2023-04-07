from exam_python_23_august_2021.project import Library
from unittest import TestCase


class TestLibrary(TestCase):

    def setUp(self):
        self.library = Library("abc")

    def test_correct_initialization(self):

        self.assertEqual("abc", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_initialization_with_wrong_name(self):

        with self.assertRaises(ValueError) as ve:
            self.library.name = ''

        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_when_author_and_title_not_added_before(self):
        self.library.add_book("Ivan Vazov", "Pod Igoto")

        self.assertEqual({"Ivan Vazov": ["Pod Igoto"]}, self.library.books_by_authors)

    def test_add_book_when_author_added_before(self):
        self.library.books_by_authors["Ivan Vazov"] = []
        self.library.add_book("Ivan Vazov", "Pod Igoto")

        self.assertEqual({"Ivan Vazov": ["Pod Igoto"]}, self.library.books_by_authors)

    def test_add_book_when_author_and_title_added_before(self):
        self.library.books_by_authors["Ivan Vazov"] = ["Pod Igoto"]
        self.library.add_book("Ivan Vazov", "Pod Igoto")

        self.assertEqual({"Ivan Vazov": ["Pod Igoto"]}, self.library.books_by_authors)

    def test_add_reader_when_reader_is_not_added_before(self):
        self.library.add_reader("Georgi")

        self.assertEqual({"Georgi": []}, self.library.readers)

    def test_add_reader_when_reader_already_added(self):
        self.library.readers["Georgi"] = []

        self.assertEqual("Georgi is already registered in the abc library.", self.library.add_reader("Georgi"))

    def test_rent_book_when_reader_not_added_in_library_readers(self):

        self.assertEqual("Georgi is not registered in the abc Library.",
                         self.library.rent_book("Georgi", "Ivan Vazov", "Pod Igoto"))

    def test_rent_book_when_author_not_added_in_library(self):
        self.library.readers["Georgi"] = []

        self.assertEqual("abc Library does not have any Ivan Vazov's books.",
                         self.library.rent_book("Georgi", "Ivan Vazov", "Pod Igoto"))

    def test_rent_book_when_book_not_added_to_authors_books(self):
        self.library.readers["Georgi"] = []
        self.library.books_by_authors["Ivan Vazov"] = []

        self.assertEqual("""abc Library does not have Ivan Vazov's "Pod Igoto".""",
                         self.library.rent_book("Georgi", "Ivan Vazov", "Pod Igoto"))

    def test_rent_book_when_all_parameters_are_valid(self):
        self.library.readers["Georgi"] = []
        self.library.books_by_authors["Ivan Vazov"] = ["Pod Igoto"]

        self.library.rent_book("Georgi", "Ivan Vazov", "Pod Igoto")

        self.assertEqual([{"Ivan Vazov": "Pod Igoto"}], self.library.readers["Georgi"])
        self.assertEqual({"Ivan Vazov": []}, self.library.books_by_authors)

