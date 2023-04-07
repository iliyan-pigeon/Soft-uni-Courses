from unittest import TestCase, main
from testing.test_cat import Cat


class CatTests(TestCase):

    def setUp(self):
        self.cat = Cat("Juicy")

    def test_correct_initialization(self):
        self.assertEqual("Juicy", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_feeding_cat_when_fed(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_if_fed_after_eating(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)

    def test_if_sleepy_after_eating(self):
        self.cat.eat()

        self.assertTrue(self.cat.sleepy)

    def test_cat_size_after_eating(self):
        self.cat.eat()

        self.assertEqual(1, self.cat.size)

    def test_sleeping_if_not_fed(self):

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_if_sleepy_after_slept(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()