from decorators_exercise.computer_store.project.computer_types.computer import Computer


class Laptop(Computer):
    AVAILABLE_PROCESSORS = {"AMD Ryzen 9 5950X": 900,
                            "Intel Core i9-11900H": 1050,
                            "Apple M1 Pro": 1200
                            }
    MAX_RAM = 64

    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor, ram):
        ram_iterations = 0
        ram_checker = ram

        if processor not in Laptop.AVAILABLE_PROCESSORS:
            raise ValueError(
                f"{self.processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if ram <= Laptop.MAX_RAM:
            while ram_checker >= 2:
                ram_iterations += 1
                ram_checker /= 2
            if ram_checker == 1.0:
                self.processor = processor
                self.ram = ram
                self.price = ram_iterations * Laptop.AVAILABLE_PROCESSORS[processor]
                return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

        return f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!"
