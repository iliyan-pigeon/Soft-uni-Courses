from exam_python_OOP_22_august_2020.project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        monthly_consumptions = 0

        for room in self.rooms:
            room_consumptions = 0

            room_consumptions += room.room_cost
            room_consumptions += room.expenses

            monthly_consumptions += room_consumptions

        return f"Monthly consumption: {monthly_consumptions:.2f}$."

    def pay(self):
        result = []

        for room in self.rooms:
            if room.expenses <= room.budget:
                new_budget = room.budget - (room.expenses + room.room_cost)
                room.budget = new_budget

                result.append(f"{room.family_name} paid {room.expenses + room.room_cost}$ and have {new_budget}$ left.")

            else:
                self.rooms.remove(room)

                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return '\n'.join(result)

    def status(self):
        result = []

        all_people_in_hotel = sum([r.members_count for r in self.rooms])
        result.append(f"Total population: {all_people_in_hotel:.2f}")

        for room in self.rooms:
            result.append(f"{room.name} with {room.members_count} members. Budget:"
                          f" {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            if room.__class__.__name__ == "YoungCoupleWithChildren":
                child_number = 1
                for ch in room.children:
                    monthly_cost = ch.cost * 30
                    result.append(f"--- Child {child_number} monthly cost: {monthly_cost:.2f}$")
                    child_number += 1

            if room.appliances:
                all_appliances_cost = sum([ap.get_monthly_expense for ap in room.appliances])
                result.append(f"--- Appliances monthly cost: {all_appliances_cost}$")

        return result
