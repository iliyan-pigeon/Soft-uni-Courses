from exam_puthon_actual_10_december_2022.project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON = 2.50

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        current_reserve_price = OpenBooth.PRICE_PER_PERSON * number_of_people

        self.price_for_reservation = current_reserve_price
        self.is_reserved = True
