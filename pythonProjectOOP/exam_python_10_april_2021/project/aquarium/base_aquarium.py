from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Aquarium name cannot be an empty string.")

        self.__name = value

    @abstractmethod
    def calculate_comfort(self):
        pass

    @abstractmethod
    def add_fish(self, fish):
        pass

    @abstractmethod
    def remove_fish(self, fish):
        pass

    @abstractmethod
    def add_decoration(self, decoration):
        pass

    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


