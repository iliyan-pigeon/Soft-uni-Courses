from exam_python_OOP_10_april_2022.project import Movie
from unittest import TestCase, main


class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie("Sparta", 2010, 8.5)

    def test_correct_initialization(self):
        self.assertEqual("Sparta", self.movie.name)
        self.assertEqual(2010, self.movie.year)
        self.assertEqual(8.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_initialization_with_wrong_data(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_when_actor_is_already_in_the_list(self):
        self.movie.actors = ["Ivan"]

        self.assertEqual("Ivan is already added in the list of actors!", self.movie.add_actor("Ivan"))

    def test_add_actor_when_actor_is_not_in_the_list(self):
        self.movie.add_actor("Ivan")

        self.assertEqual(["Ivan"], self.movie.actors)

    def test_gt_magic_method_if_self_rating_is_better_than_other(self):
        other = Movie("abc", 2000, 8.0)

        self.assertEqual('"Sparta" is better than "abc"', self.movie.__gt__(other))

    def test_gt_magic_method_if_other_rating_is_better_than_self(self):
        other = Movie("abc", 2000, 8.6)

        self.assertEqual('"abc" is better than "Sparta"', self.movie.__gt__(other))

    def test_repr_magic_method(self):
        self.movie.actors = ["Ivan", "Georgi"]

        self.assertEqual(f"Name: {self.movie.name}\n"
                         f"Year of Release: {self.movie.year}\n"
                         f"Rating: {self.movie.rating:.2f}\n"
                         f"Cast: {', '.join(self.movie.actors)}", str(self.movie))


if __name__ == '__main__':
    main()
