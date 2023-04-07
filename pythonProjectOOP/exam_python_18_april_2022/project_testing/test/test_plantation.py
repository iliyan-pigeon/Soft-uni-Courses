from exam_python_18_april_2022.project import Plantation
from unittest import TestCase


class TestPlantation(TestCase):

    def setUp(self):
        self.plantation = Plantation(10)
        self.plants_dict = {"Ivan": ["rose", "tulip"],
                            "Georgi": ["Snowflake", "hyacinth"]}
        self.workers_list = ["Ivan", "Georgi"]

    def test_correct_initialization_with_valid_size(self):

        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_correct_initialization_with_not_valid_size(self):

        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_when_worker_already_hired(self):
        self.plantation.workers.append("Ivan")

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Ivan")

        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_when_worker_not_hired(self):

        self.assertEqual("Ivan successfully hired.", self.plantation.hire_worker("Ivan"))
        self.assertEqual(["Ivan"], self.plantation.workers)

    def test_len_magic_method(self):
        self.plantation.plants = self.plants_dict

        self.assertEqual(4, len(self.plantation))

    def test_planting_when_worker_not_hired(self):

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Ivan", "rose")

        self.assertEqual("Worker with name Ivan is not hired!", str(ve.exception))

    def test_planting_when_there_is_no_free_space_to_plant(self):
        self.plantation.size = 4
        self.plantation.workers = self.workers_list
        self.plantation.plants = self.plants_dict

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Ivan", "rose")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_when_worker_already_planted_before(self):
        self.plantation.plants = self.plants_dict
        self.plantation.workers = self.workers_list

        self.assertEqual("Ivan planted rose.", self.plantation.planting("Ivan", "rose"))
        self.assertEqual({"Ivan": ["rose", "tulip", "rose"],
                            "Georgi": ["Snowflake", "hyacinth"]}, self.plantation.plants)

    def test_planting_when_worker_plants_for_the_first_time(self):
        self.plantation.workers = self.workers_list

        self.assertEqual("Ivan planted it's first rose.", self.plantation.planting("Ivan", "rose"))
        self.assertEqual({"Ivan": ["rose"]}, self.plantation.plants)

    def test_str_representation_of_the_class(self):
        self.plantation.workers = self.workers_list
        self.plantation.plants = self.plants_dict

        self.assertEqual("Plantation size: 10\n"
                         "Ivan, Georgi\n"
                         "Ivan planted: rose, tulip\n"
                         "Georgi planted: Snowflake, hyacinth", str(self.plantation))

    def test_repr_representation_of_the_class(self):
        self.plantation.workers = self.workers_list

        self.assertEqual("Size: 10\nWorkers: Ivan, Georgi", self.plantation.__repr__())

