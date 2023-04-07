from unittest import TestCase, main
from testing_exercise.vehicle.project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(10.5, 100)

    def test_default_attributes(self):

        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_initialization(self):

        self.assertEqual(10.5, self.vehicle.fuel)
        self.assertEqual(10.5, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_driving_if_not_enough_fuel(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_driving_if_fuel_is_enough(self):
        self.vehicle.drive(1)

        self.assertEqual(9.25, self.vehicle.fuel)

    def test_refuel_if_fuel_is_too_munch(self):
        self.vehicle.fuel = 8.5

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(5)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_if_fuel_is_not_too_much(self):
        self.vehicle.fuel = 8.5
        self.vehicle.refuel(1)

        self.assertEqual(9.5, self.vehicle.fuel)

    def test_if_str_representation_is_correct(self):

        self.assertEqual("The vehicle has 100 "
               "horse power with 10.5 fuel left and 1.25 fuel consumption", str(self.vehicle))


if __name__ == '__main__':
    main()
