from exam_puthon_actual_10_december_2022.project.booths.open_booth import OpenBooth
from exam_puthon_actual_10_december_2022.project.booths.private_booth import PrivateBooth
from exam_puthon_actual_10_december_2022.project.delicacies.gingerbread import Gingerbread
from exam_puthon_actual_10_december_2022.project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in [d.name for d in self.delicacies]:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in ["Gingerbread", "Stolen"]:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if type_delicacy == "Gingerbread":
            current_delicacy = Gingerbread(name, price)
            self.delicacies.append(current_delicacy)

        elif type_delicacy == "Stolen":
            current_delicacy = Stolen(name, price)
            self.delicacies.append(current_delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ["Open Booth", "Private Booth"]:
            raise Exception(f"{type_booth} is not a valid booth!")

        if type_booth == "Open Booth":
            current_booth = OpenBooth(booth_number, capacity)
            self.booths.append(current_booth)

        elif type_booth == "Private Booth":
            current_booth = PrivateBooth(booth_number, capacity)
            self.booths.append(current_booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        the_booth = [b for b in self.booths if b.booth_number == booth_number]
        the_delicacy = [d for d in self.delicacies if d.name == delicacy_name]

        if not the_booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not the_delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth = the_booth[0]
        delicacy = the_delicacy[0]

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]

        bill_amount = booth.price_for_reservation + sum([d.price for d in booth.delicacy_orders])
        self.income += bill_amount

        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {bill_amount:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
