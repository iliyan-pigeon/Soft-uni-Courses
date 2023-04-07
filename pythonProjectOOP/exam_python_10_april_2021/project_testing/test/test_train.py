from unittest import TestCase, main
from exam_python_10_april_2021.project import Train


class TestTrain(TestCase):

    def setUp(self):
        self.train = Train("diablo", 10)

    def test_correct_initialization(self):

        self.assertEqual("diablo", self.train.name)
        self.assertEqual(10, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passenger_when_capacity_is_full(self):
        self.train.capacity = 1
        self.train.passengers.append("Jon")

        with self.assertRaises(ValueError) as ve:
            self.train.add("Mickael")
        self.assertEqual("Train is full", str(ve.exception))

    def test_add_passenger_when_passenger_already_added(self):
        self.train.passengers.append("Jon")

        with self.assertRaises(ValueError) as ve:
            self.train.add("Jon")
        self.assertEqual("Passenger Jon Exists", str(ve.exception))

    def test_add_passenger_when_everything_is_good(self):

        self.assertEqual("Added passenger Jon", self.train.add("Jon"))
        self.assertEqual(["Jon"], self.train.passengers)

    def test_remove_passenger_when_passenger_does_not_exist(self):

        with self.assertRaises(ValueError) as ve:
            self.train.remove("Jon")
        self.assertEqual("Passenger Not Found", str(ve.exception))

    def test_remove_passenger_when_passenger_exists(self):
        self.train.passengers.append("Jon")

        self.assertEqual("Removed Jon", self.train.remove("Jon"))
        self.assertEqual([], self.train.passengers)


if __name__ == '__main__':
    main()
