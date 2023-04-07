from exam_python_OOP_15_august_2021.project.baked_food.bread import Bread
from exam_python_OOP_15_august_2021.project.baked_food.cake import Cake
from exam_python_OOP_15_august_2021.project.drink.tea import Tea
from exam_python_OOP_15_august_2021.project.drink.water import Water
from exam_python_OOP_15_august_2021.project.table.inside_table import InsideTable
from exam_python_OOP_15_august_2021.project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if name in [f.name for f in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type == "Bread":
            food = Bread(name, price)
            self.food_menu.append(food)

        elif food_type == "Cake":
            food = Cake(name, price)
            self.food_menu.append(food)

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if name in [d.name for d in self.drinks_menu]:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type == "Tea":
            drink = Tea(name, portion, brand)
            self.drinks_menu.append(drink)

        elif drink_type == "Water":
            drink = Water(name, portion, brand)
            self.drinks_menu.append(drink)

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_number in [t.table_number for t in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
            self.tables_repository.append(table)

        elif table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)
            self.tables_repository.append(table)

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *foods_names):
        for table in self.tables_repository:
            if table.number == table_number:
                to_add = []
                not_on_the_menu = []

                for food_name in foods_names:
                    if food_name in [f.name for f in self.food_menu]:
                        food = [f for f in self.food_menu if f.name == food_name][0]
                        to_add.append(food)

                    else:
                        not_on_the_menu.append(food_name)

                result = f"Table {table_number} ordered:\n"

                for food in to_add:
                    result += f"{repr(food)}\n"
                    table.food_orders.append(food)

                result += f"{self.name} does not have in the menu:\n"

                for food in not_on_the_menu:
                    result += f"{food.name}\n"

                return result.rstrip()

        return f"Could not find table {table_number}"

    def order_drink(self, table_number: int, *drinks_names):
        for table in self.tables_repository:
            if table.number == table_number:
                to_add = []
                not_on_the_menu = []

                for drink_name in drinks_names:
                    if drink_name in [d.name for d in self.drinks_menu]:
                        drink = [d for d in self.drinks_menu if d.name == drink_name]
                        to_add.append(drink)

                    else:
                        not_on_the_menu.append(drink_name)

                result = [f"Table {table_number} ordered:"]

                for drink in to_add:
                    result.append(repr(drink))
                    table.drink_orders.append(drink)

                result.append(f"{self.name} does not have in the menu:")

                for drink in not_on_the_menu:
                    result.append(drink.name)

                return "\n".join(result)

        return f"Could not find table {table_number}"

    def leave_table(self, table_number):
        table = [table for table in self.tables_repository if table.table_number == table_number]
        if table:
            the_table = table[0]
            the_table.clear()

            result = f"Table: {table_number}\nBill: {the_table.get_bill():.2f}"

            return result

    def get_free_tables_info(self):
        free_tables = [table for table in self.tables_repository if not table.is_reserved]
        result = []

        for t in free_tables:
            result.append(t.free_table_info())

        result = "\n".join(result)
        return result

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
