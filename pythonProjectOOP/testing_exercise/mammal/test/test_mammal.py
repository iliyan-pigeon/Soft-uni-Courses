from unittest import TestCase, main
from testing_exercise.mammal.project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Demon", "dog", "bark")

    def test_correct_initialization(self):

        self.assertEqual("Demon", self.mammal.name)
        self.assertEqual("dog", self.mammal.type)
        self.assertEqual("bark", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_is_make_sound_function_works_properly(self):

        self.assertEqual("Demon makes bark", self.mammal.make_sound())

    def test_is_get_kingdom_function_works_properly(self):

        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_is_info_function_returns_the_proper_information(self):

        self.assertEqual("Demon is of type dog", self.mammal.info())


if __name__ == '__main__':
    main()


