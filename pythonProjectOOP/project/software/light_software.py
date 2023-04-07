from project.software.software import Software


class LightSoftware(Software):
    TYPE = "Light"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        capacity_consumption = int(capacity_consumption + (capacity_consumption / 2))
        memory_consumption = int(memory_consumption - (memory_consumption / 2))
        super().__init__(name, LightSoftware.TYPE, capacity_consumption, memory_consumption)
