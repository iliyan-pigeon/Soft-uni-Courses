from exam_python_OOP_10_april_2022.project import Movie


class Thriller(Movie):
    DEFAULT_AGE_RESTRICTION = 16

    def __init__(self, title: str, year: int, owner: object, age_restriction=DEFAULT_AGE_RESTRICTION):
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}," \
               f" Age restriction:{self.age_restriction}," \
               f" Likes:{self.likes}, Owned by:{self.owner.username}"
