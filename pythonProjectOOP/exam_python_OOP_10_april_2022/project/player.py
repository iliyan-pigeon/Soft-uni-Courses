class Player:
    USED_NAMES = []

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.__need_sustenance = True


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")

        if value in Player.USED_NAMES:
            raise Exception(f"Name {value} is already used!")

        Player.USED_NAMES.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value > 100:
            raise ValueError("Stamina not valid!")
        if value < 0:
            raise ValueError("Stamina not valid!")

        self.__stamina = value

    @property
    def need_sustenance(self):
        if self.stamina < 100:
            return self.__need_sustenance

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
