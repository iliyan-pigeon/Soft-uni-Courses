from project.hardware.hardware import Hardware
from project.software.software import Software


class HeavyHardware(Hardware):
    TYPE = "Heavy"

    def __init__(self, name: str, capacity: int, memory: int):
        capacity *= 2
        memory = int(memory * 0.75)
        super().__init__(name, HeavyHardware.TYPE, capacity, memory)

    def install(self, software: Software):
        if software.memory_consumption > self.memory or software.capacity_consumption > self.capacity:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.software_components.remove(software)
