from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        ...


class Dog(Animal):
    def make_sound(self):
        return "Woof woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow meow"


class Horse(Animal):
    def make_sound(self):
        return "Iighhaaa"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat(), Horse()]
animal_sound(animals)


