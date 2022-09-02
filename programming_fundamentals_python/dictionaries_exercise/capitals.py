countries = input().split(", ")
capitals = input().split(", ")
pairs_dict = {countries[index]: capitals[index] for index in range(len(countries))}
for key in pairs_dict:
    print(f"{key} -> {pairs_dict[key]}")


