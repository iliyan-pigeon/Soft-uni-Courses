from unittest import TestCase, main
from testing.test_worker import Worker


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker("Hard worker", 1000, 100)

    def test_correct_initialization(self):
        self.assertEqual("Hard worker", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_working_if_energy_is_zero(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_money_when_receiving_salary(self):
        self.worker.work()

        self.assertEqual(1000, self.worker.money)

    def test_energy_when_decreased(self):
        self.worker.work()

        self.assertEqual(99, self.worker.energy)

    def test_energy_after_resting(self):
        self.worker.rest()

        self.assertEqual(101, self.worker.energy)

    def test_get_info_method(self):

        self.assertEqual('Hard worker has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    main()
