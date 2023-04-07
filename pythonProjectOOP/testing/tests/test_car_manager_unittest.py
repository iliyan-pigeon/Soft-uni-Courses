from unittest import TestCase, main
#from testing.car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("Kia", "Ceed", 10, 100)

    def test_correct_initialization(self):
        self.assertEqual("Kia", self.car.make)
        self.assertEqual("Ceed", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_when_null_or_empty(self):

        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_when_null_or_empty(self):

        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_when_fuel_consumption_is_zero_or_negative(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_when_fuel_capacity_is_zero_or_negative(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_when_fuel_amount_is_negative(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_when_refueled_fuel_amount_is_negative(self):

        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_when_refueled_fuel_amount_is_correct(self):
        self.car.refuel(10)

        self.assertEqual(10, self.car.fuel_amount)

    def test_when_refueled_fuel_amount_is_correct_but_exceed_capacity(self):
        self.car.refuel(101)

        self.assertEqual(100, self.car.fuel_amount)

    def test_when_fuel_is_not_enough_for_the_drive(self):

        with self.assertRaises(Exception) as ex:
            self.car.drive(11)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_when_fuel_for_the_drive_is_enough(self):
        self.car.fuel_amount = 100
        self.car.drive(1000)

        self.assertEqual(0, self.car.fuel_amount)


if __name__ == '__main__':
    main()
