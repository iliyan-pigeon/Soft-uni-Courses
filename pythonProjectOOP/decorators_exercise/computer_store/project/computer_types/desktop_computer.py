from decorators_exercise.computer_store.project.computer_types.computer import Computer


class DesktopComputer(Computer):
    AVAILABLE_PROCESSORS = {"AMD Ryzen 7 5700G": 500,
                            "Intel Core i5-12600K": 600,
                            "Apple M1 Max": 1800
                            }
    MAX_RAM = 128

    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor, ram):
        ram_iterations = 0
        ram_checker = ram

        if processor not in DesktopComputer.AVAILABLE_PROCESSORS:
            raise ValueError(f"{self.processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram <= DesktopComputer.MAX_RAM:
            while ram_checker >= 2:
                ram_iterations += 1
                ram_checker /= 2
            if ram_checker == 1.0:
                self.processor = processor
                self.ram = ram
                self.price = ram_iterations * DesktopComputer.AVAILABLE_PROCESSORS[processor]
                return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

        return f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!"



