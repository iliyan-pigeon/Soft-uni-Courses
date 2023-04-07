class Client:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        v = value.startswith("0")
        if v and all([i.isdigit() for i in value]) and len(value) == 10:
            self.__phone_number = value
        else:
            raise ValueError("Invalid phone number!")
