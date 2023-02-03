def grocery_store(**kwargs):
    final_string = ''
    kwargs = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    for key, value in kwargs.items():
        final_string += f"{key}: {value}\n"
    return final_string


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
