from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"

        hardware = hardware[0]
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)

        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"

        hardware = hardware[0]
        software = LightSoftware(name, capacity_consumption, memory_consumption)

        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        software = [s for s in System._software if s.name == software_name]

        if not hardware or not software:
            return "Some of the components do not exist"

        hardware = hardware[0]
        software = software[0]

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        hardware_components_amount = len(System._hardware)
        software_components_amount = len(System._software)
        total_memory_consumption = sum([s.memory_consumption for s in System._software])
        total_memory = sum([h.memory for h in System._hardware])
        total_capacity_consumption = sum([s.capacity_consumption for s in System._software])
        total_capacity = sum([h.capacity for h in System._hardware])

        result = "System Analysis\n"
        result += f"Hardware Components: {hardware_components_amount}\n"
        result += f"Software Components: {software_components_amount}\n"
        result += f"Total Operational Memory: {total_memory_consumption} / {total_memory}\n"
        result += f"Total Capacity Taken: {total_capacity_consumption} / {total_capacity}"

        return result

    @staticmethod
    def system_split():
        result = ''

        for hardware in System._hardware:
            name = hardware.name
            express_software_amount = [s for s in hardware.software_components if s.__type__.__name__ == "Express"]
            light_software_amount = [s for s in hardware.software_components if s.__type__.__name__ == "Light"]
            total_memory_consumption = sum([s.memory_consumption for s in hardware.software_components])
            total_memory = hardware.memory
            total_capacity_consumption = sum([s.capacity_consumption for s in hardware.software_components])
            total_capacity = hardware.capacity
            hardware_type = hardware.__type__.__name__
            software_components_names = [s.name for s in hardware.software_components]
            if not software_components_names:
                software_components_names = "None"
            else:
                software_components_names = ", ".join(software_components_names)

            result += f"Hardware Component - {name}"
            result += f"Express Software Components: {express_software_amount}"
            result += f"Light Software Components: {light_software_amount}"
            result += f"Memory Usage: {total_memory_consumption} / {total_memory}"
            result += f"Capacity Usage: {total_capacity_consumption} / {total_capacity}"
            result += f"Type: {hardware_type}"
            result += f"Software Components: {software_components_names}"

        return result.strip()
