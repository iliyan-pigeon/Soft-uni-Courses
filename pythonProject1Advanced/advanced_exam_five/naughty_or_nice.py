def naughty_or_nice_list(some_list, *args, **kwargs):
    nice = []
    naughty = []
    not_found = []
    result = ''
    counter = 0

    for arg in args:
        searched_number = int(arg.split("-")[0])
        definition = arg.split("-")[1]
        for kid in some_list:
            if searched_number == kid[0]:
                counter += 1
        for kid in some_list:
            if counter == 1 and searched_number == kid[0]:
                if definition == "Nice":
                    nice.append(kid[1])
                elif definition == "Naughty":
                    naughty.append(kid[1])
        counter = 0

    for key, value in kwargs.items():
        searched_name = key
        definition = value
        for kid in some_list:
            if searched_name == kid[1]:
                counter += 1
        for kid in some_list:
            if counter == 1 and searched_name == kid[1]:
                if definition == "Nice":
                    nice.append(kid[1])
                elif definition == "Naughty":
                    naughty.append(kid[1])
        counter = 0

    for kid in some_list:
        if kid[1] not in nice and kid[1] not in naughty:
            not_found.append(kid[1])

    if nice:
        result += f"Nice: {', '.join(nice)}\n"
    if naughty:
        result += f"Naughty: {', '.join(naughty)}\n"
    if not_found:
        result += f"Not found: {', '.join(not_found)}"

    return result


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))