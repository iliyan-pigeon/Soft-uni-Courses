def even_odd(*args):
    command = args[-1]
    filtered_numbers = []
    if command == "odd":
        filtered_numbers = [i for i in args[:-1] if i % 2 != 0]
    elif command == "even":
        filtered_numbers = [i for i in args[:-1] if i % 2 == 0]
    return filtered_numbers


print(even_odd(1, 2, 3, 4, 5, 6, "even"))