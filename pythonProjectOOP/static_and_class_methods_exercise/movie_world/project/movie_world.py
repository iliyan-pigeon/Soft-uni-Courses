class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if MovieWorld.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if MovieWorld.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        age_restriction = 0
        for c in self.customers:
            if c.id == customer_id:
                for dvd in c.rented_dvds:
                    if dvd.id == dvd_id:
                        return f"{c.name} has already rented {dvd.name}"

        for dvd in self.dvds:
            if dvd.id == dvd_id:
                age_restriction = dvd.age_restriction
                if dvd.is_rented:
                    return "DVD is already rented"

        for c in self.customers:
            if c.id == customer_id:
                if c.age < age_restriction:
                    return f"{c.name} should be at least {age_restriction} to rent this movie"

        for c in self.customers:
            if c.id == customer_id:
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        c.rented_dvds.append(dvd)
                        dvd.is_rented = True
                        return f"{c.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):

        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        dvd.is_rented = False
                        customer.rented_dvds.remove(dvd)
                        return f"{customer.name} has successfully returned {dvd.name}"
                return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''

        for customer in self.customers:
            result += f"{customer}\n"

        for dvd in self.dvds:
            if dvd == self.dvds[-1]:
                result += f"{dvd}"
            else:
                result += f"{dvd}\n"

        return result
