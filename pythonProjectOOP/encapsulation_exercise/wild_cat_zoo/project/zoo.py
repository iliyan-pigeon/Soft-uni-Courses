class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals):
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        combined_salaries = 0

        for w in self.workers:
            combined_salaries += w.salary

        if self.__budget >= combined_salaries:
            self.__budget -= combined_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        combined_care_money = 0

        for a in self.animals:
            combined_care_money += a.money_for_care

        if self.__budget >= combined_care_money:
            self.__budget -= combined_care_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = []
        tigers = []
        cheetahs = []

        for a in self.animals:
            if a.__class__.__name__ == "Lion":
                lions.append(a)
            elif a.__class__.__name__ == "Tiger":
                tigers.append(a)
            elif a.__class__.__name__ == "Cheetah":
                cheetahs.append(a)

        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += lion.__repr__() + "\n"
        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += tiger.__repr__() + "\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            if cheetah == cheetahs[-1]:
                result += cheetah.__repr__()
            else:
                result += cheetah.__repr__() + "\n"

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = []
        caretakers = []
        vets = []

        for w in self.workers:
            if w.__class__.__name__ == "Keeper":
                keepers.append(w)
            elif w.__class__.__name__ == "Caretaker":
                caretakers.append(w)
            elif w.__class__.__name__ == "Vet":
                vets.append(w)

        result += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += keeper.__repr__() + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += caretaker.__repr__() + "\n"
        result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            if vet == vets[-1]:
                result += vet.__repr__()
            else:
                result += vet.__repr__() + "\n"

        return result



