def forecast(*args):
    result = ''
    weather_dict = {"Sunny": [], "Cloudy": [], "Rainy": []}

    for arg in args:
        location = arg[0]
        weather = arg[1]

        if weather == "Sunny":
            weather_dict[weather].append(location)
        elif weather == "Rainy":
            weather_dict[weather].append(location)
        elif weather == "Cloudy":
            weather_dict[weather].append(location)

    for key, value in weather_dict.items():
        value = sorted(value)

        for location in value:
            result += f"{location} - {key}\n"

    return result


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))