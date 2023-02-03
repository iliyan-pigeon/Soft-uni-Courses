def age_assignment(*args, **kwargs):
    people_data = {}
    result = ''
    for person in args:
        people_data[person] = 0
    for key, value in kwargs.items():
        for person in people_data:
            if key in person:
                people_data[person] = value
    people_data = dict(sorted(people_data.items(), key=lambda x: x))
    for key, value in people_data.items():
        result += f"{key} is {value} years old.\n"
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36,
                     A=22, B=61))
