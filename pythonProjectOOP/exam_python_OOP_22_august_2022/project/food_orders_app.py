from exam_python_OOP_22_august_2022.project.client import Client


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 0

    def register_client(self, client_phone_number):
        if [True for cl in self.clients_list if cl.phone_number == client_phone_number]:
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            meal_type = meal.__class__.__name__
            if meal_type == "Starter" or meal_type == "MainDish" or meal_type == "Dessert":
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = ''
        for meal in self.menu:
            result += meal.details() + "\n"

        return result

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        registered = False
        the_client = ''
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                registered = True
                the_client = client

        if not registered:
            self.register_client(client_phone_number)
            the_client = [client for client in self.clients_list if client.phone_number == client_phone_number][0]

        current_bill = 0
        products_to_add = []

        for meal, quantity in meal_names_and_quantities.items():
            found_product = False
            for product in self.menu:
                if product.name == meal:
                    found_product = True
                    if product.quantity >= quantity:
                        products_to_add.append([meal, quantity])
                        product.quantity -= quantity
                        current_bill += product.price * quantity
                        break
                    else:
                        raise Exception(f"Not enough quantity of {product.__class__.__name__}: {product.name}!")
            if not found_product:
                raise Exception(f"{meal} is not on the menu!")

        the_client.bill += current_bill
        the_client.shopping_cart += products_to_add
        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join([meal[0] for meal in the_client.shopping_cart])} for {the_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        the_client = [client for client in self.clients_list if client.phone_number == client_phone_number][0]

        if not the_client.shopping_cart:
            raise Exception("There are no ordered meals!")

        the_client.bill = 0
        for meal in the_client.shopping_cart:
            for product in self.menu:
                if product.name == meal[0]:
                    product.quantity += meal[1]
                    break
        the_client.shopping_cart.clear()
        return f"Client {the_client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        the_client = [client for client in self.clients_list if client.phone_number == client_phone_number][0]

        if not the_client.shopping_cart:
            raise Exception("There are no ordered meals!")

        bill = the_client.bill
        the_client.bill = 0
        the_client.shopping_cart.clear()
        self.receipt_id += 1

        return f"Receipt #{self.receipt_id} with total amount of {bill:.2f}" \
               f" was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


from exam_python_OOP_22_august_2022.project.meals.starter import Starter
from exam_python_OOP_22_august_2022.project.meals.dessert import Dessert
from exam_python_OOP_22_august_2022.project.meals.main_dish import MainDish

food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
print(food_orders_app.register_client("0894944732"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
print(food_orders_app.finish_order("0899999999"))
print(food_orders_app)
