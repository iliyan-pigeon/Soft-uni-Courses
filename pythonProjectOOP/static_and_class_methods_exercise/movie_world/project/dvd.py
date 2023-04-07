from calendar import month_name


class DVD:
    def __init__(self, name, id_number, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id_number
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id_number, name, date, age_restriction):
        date = date.split(".")
        creation_year = date[2]
        creation_month = date[1]
        return cls(name, id_number, creation_year, month_name[creation_month] , age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"
