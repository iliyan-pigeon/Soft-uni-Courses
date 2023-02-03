def get_info(**kwargs):
    name = kwargs["name"]
    town = kwargs["town"]
    age = kwargs["age"]
    return f"This is {name} from {town} and he is {age} years old"


person = {"name": "George", "town":"Sofia", "age": 20}
print(get_info(**person))

