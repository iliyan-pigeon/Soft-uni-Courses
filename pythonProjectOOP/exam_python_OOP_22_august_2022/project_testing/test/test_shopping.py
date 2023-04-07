from exam_python_OOP_22_august_2022.project_testing.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self):
        self.cart = ShoppingCart("Name", 100)

    def test_initialization_if_name_starts_with_lower_letter(self):

        with self.assertRaises(ValueError) as ve:
            self.cart = ShoppingCart("name", 100)

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_initialization_if_name_have_not_only_letters(self):

        with self.assertRaises(ValueError) as ve:
            self.cart = ShoppingCart("Na4e", 100)

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_correct_initialization_if_name_is_valid(self):

        self.assertEqual("Name", self.cart.shop_name)
        self.assertEqual(100, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_add_to_cart_when_product_cost_too_much(self):

        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("pasta", 100)

        self.assertEqual("Product pasta cost too much!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("pasta", 101)

        self.assertEqual("Product pasta cost too much!", str(ve.exception))

    def test_add_to_cart_when_product_is_affordable(self):

        self.assertEqual("pasta product was successfully added to the cart!", self.cart.add_to_cart("pasta", 90))
        self.assertEqual(90, self.cart.products["pasta"])

    def test_remove_from_cart_when_product_is_not_in_the_cart(self):

        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("pasta")

        self.assertEqual("No product with name pasta in the cart!", str(ve.exception))

    def test_remove_from_cart_when_product_is_in_the_cart(self):
        self.cart.products["pasta"] = 90

        self.assertEqual("Product pasta was successfully removed from the cart!", self.cart.remove_from_cart("pasta"))
        self.assertEqual([], [True for i in self.cart.products if i == "pasta"])

    def test_to_add_another_instance_of_a_cart_to_the_old_one(self):
        new_cart = ShoppingCart("New", 100)

        self.assertEqual(new_cart, self.cart.__add__(new_cart))


if __name__ == '__main__':
    main()
