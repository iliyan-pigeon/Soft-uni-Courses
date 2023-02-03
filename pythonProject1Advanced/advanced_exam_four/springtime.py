def start_spring(**kwargs):
    result = ''
    types_dictionary = {}

    for key, value in kwargs.items():
        if value not in types_dictionary:
            types_dictionary[value] = []
        types_dictionary[value].append(key)
    types_dictionary = sorted(types_dictionary.items(), key=lambda x: (-len(x[1]), x[0]))

    for type in types_dictionary:
        ordered_elements = sorted(type[1])
        result += f"{type[0]}:\n"
        for element in ordered_elements:
            result += f"-{element}\n"

    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))