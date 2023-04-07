from unittest import TestCase, main
from testing.extended_list import IntegerList


class ListTests(TestCase):

    def setUp(self):
        self.list = IntegerList(1,2,3, "1", "2", "3", "Alaska")

    def test_correct_initialization(self):
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

    def test_if_get_data_works_properly(self):
        self.assertEqual([1, 2, 3], self.list.get_data())

    def test_adding_element_when_not_integer(self):

        with self.assertRaises(ValueError) as ve:
            self.list.add("1")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_adding_element_when_integer(self):
        result = self.list.add(4)

        self.assertEqual([1, 2, 3, 4], result)
        self.assertEqual([1, 2, 3, 4], self.list._IntegerList__data)

    def test_remove_when_index_out_of_range(self):

        with self.assertRaises(IndexError) as ie:
            self.list.remove_index(3)

        self.assertEqual("Index is out of range", str(ie.exception))

        with self.assertRaises(IndexError) as ie:
            self.list.remove_index(4)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_when_index_in_range(self):
        a = self.list.remove_index(2)

        self.assertEqual(3, a)
        self.assertEqual([1, 2], self.list._IntegerList__data)

    def test_get_when_index_out_of_range(self):

        with self.assertRaises(IndexError) as ie:
            self.list.get(3)

        self.assertEqual("Index is out of range", str(ie.exception))

        with self.assertRaises(IndexError) as ie:
            self.list.get(4)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_when_index_in_range(self):

        self.assertEqual(1, self.list.get(0))

    def test_insert_when_index_out_of_range(self):

        with self.assertRaises(IndexError) as ie:
            self.list.insert(3, 1)

        self.assertEqual("Index is out of range", str(ie.exception))

        with self.assertRaises(IndexError) as ie:
            self.list.insert(4, 1)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_when_element_not_integer(self):

        with self.assertRaises(ValueError) as ve:
            self.list.insert(0, "1")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_when_parameters_are_right(self):
        self.list.get_data().insert(3, 4)

        self.assertEqual([1, 2, 3, 4], self.list._IntegerList__data)

    def test_get_biggest_number(self):

        self.assertEqual(3, self.list.get_biggest())

    def test_getting_index_of_element(self):

        self.assertEqual(1, self.list.get_index(2))


if __name__ == '__main__':
    main()