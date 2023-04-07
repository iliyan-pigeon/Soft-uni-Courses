from unittest import TestCase, main
from testing_exercise.hero.project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("pigeon", 10, 100.0, 10.0)

    def test_correct_initialization(self):
        self.assertEqual("pigeon", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(10.0, self.hero.damage)

    def test_battle_if_enemy_name_equals_your_name(self):
        enemy_hero = Hero("pigeon", 10, 100.0, 10.0)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_if_your_health_is_lower_than_zero_and_below_zero(self):
        enemy_hero = Hero("lion", 10, 100.0, 10.0)

        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

        self.hero.health = -1
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_if_enemy_health_is_lower_than_zero_and_below_zero(self):
        enemy_hero = Hero("lion", 10, 0, 10.0)

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy_hero)

        self.assertEqual("You cannot fight lion. He needs to rest", str(ve.exception))

        enemy_hero.health = -1
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy_hero)

        self.assertEqual("You cannot fight lion. He needs to rest", str(ve.exception))

    def test_battle_if_the_outcome_is_draw_with_zero_health_and_below(self):
        enemy_hero = Hero("lion", 10, 100.0, 10.0)
        self.assertEqual("Draw", self.hero.battle(enemy_hero))

        enemy_hero = Hero("lion", 11, 100.0, 10.0)
        self.hero.level = 11
        self.hero.health = 100.0
        self.assertEqual("Draw", self.hero.battle(enemy_hero))

    def test_battle_if_you_won_with_enemy_health_zero_and_below(self):
        enemy_hero = Hero("lion", 5, 100.0, 10.0)

        self.assertEqual("You win", self.hero.battle(enemy_hero))
        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(15.0, self.hero.damage)

        enemy_hero.health = 100.0
        self.assertEqual("You win", self.hero.battle(enemy_hero))
        self.assertEqual(12, self.hero.level)
        self.assertEqual(10, self.hero.health)
        self.assertEqual(20.0, self.hero.damage)

    def test_battle_if_enemy_won_with_your_health_zero_and_below(self):
        enemy_hero = Hero("lion", 10, 100.0, 10.0)
        self.hero.level = 5

        self.assertEqual("You lose", self.hero.battle(enemy_hero))
        self.assertEqual(11, enemy_hero.level)
        self.assertEqual(55, enemy_hero.health)
        self.assertEqual(15.0, enemy_hero.damage)

        self.hero.health = 100.0
        self.assertEqual("You lose", self.hero.battle(enemy_hero))
        self.assertEqual(12, enemy_hero.level)
        self.assertEqual(10, enemy_hero.health)
        self.assertEqual(20.0, enemy_hero.damage)

    def test_if_string_representation_is_correct(self):
        self.assertEqual("Hero pigeon: 10 lvl\n"
                         "Health: 100.0\n"
                         "Damage: 10.0\n", str(self.hero))


if __name__ == '__main__':
    main()
