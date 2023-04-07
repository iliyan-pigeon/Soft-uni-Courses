from exam_python_OOP_15_august_2021.project import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self):
        self.store = ToyStore()

    def test_correct_initialization(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)

    def test_add_toy_when_shelf_does_not_exist_in_the_store(self):

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("K", "doll")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_when_the_toy_is_already_on_the_shelf(self):
        self.store.toy_shelf["A"] = "doll"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "doll")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_when_the_shelf_is_taken(self):
        self.store.toy_shelf["A"] = "doll"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "car")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_when_all_data_is_correct(self):

        self.assertEqual("Toy:doll placed successfully!", self.store.add_toy("A", "doll"))
        self.assertEqual("doll", self.store.toy_shelf["A"])

    def test_remove_toy_from_shelf_when_shelf_does_not_exist(self):

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("M", "doll")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_from_shelf_when_the_toy_is_not_on_the_shelf(self):
        self.store.toy_shelf["B"] = "doll"

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("B", "car")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_from_shelf_when_the_toy_is_on_the_shelf(self):
        self.store.toy_shelf["B"] = "doll"

        self.assertEqual("Remove toy:doll successfully!", self.store.remove_toy("B", "doll"))
        self.assertEqual(None, self.store.toy_shelf["B"])


if __name__ == '__main__':
    main()