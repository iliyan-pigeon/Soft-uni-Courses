from decorators_exercise.computer_store.project.computer_types.desktop_computer import DesktopComputer
from decorators_exercise.computer_store.project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_COMPUTER_TYPES = ["Desktop Computer", "Laptop"]

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer, manufacturer, model, processor, ram):

        if type_computer in ComputerStoreApp.VALID_COMPUTER_TYPES:
            if type_computer == "Desktop Computer":
                computer = DesktopComputer(manufacturer, model)
                computer.configure_computer(processor, ram)
                self.warehouse.append(computer)
                return computer

            elif type_computer == "Laptop":
                computer = Laptop(manufacturer, model)
                computer.configure_computer(processor, ram)
                self.warehouse.append(computer)
                return computer

        return f"{type_computer} is not a valid type computer!"

    def sell_computer(self, client_budget, wanted_processor, wanted_ram):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor \
                    and computer.ram >= wanted_ram:
                self.profits = abs(client_budget - computer.price)
                self.warehouse.remove(computer)
                return f"{computer} sold for {client_budget}$."

        return "Sorry, we don't have a computer for you."
