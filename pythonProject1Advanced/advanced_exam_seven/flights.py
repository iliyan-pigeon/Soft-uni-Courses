def flights(*args):
    flights_data = {}
    last_destination = ''

    for arg in args:
        arg = str(arg)
        if arg == "Finish":
            break
        elif arg.isalpha() or " " in arg:
            last_destination = arg
            if last_destination not in flights_data:
                flights_data[last_destination] = 0
        elif arg.isdigit():
            flights_data[last_destination] += int(arg)

    return flights_data


print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))