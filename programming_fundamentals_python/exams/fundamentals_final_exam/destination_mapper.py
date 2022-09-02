places = input()
valid_places = []
store = False
validator = ""
valid = False
current_place = ""
travel_points = 0
for ch in places:
    if not ch.isalpha() and not ch.isdigit():
        if store:
            if ch == validator and len(current_place) >= 3 and current_place[0].isupper() and current_place.isalpha():
                valid = True
            if valid:
                valid_places.append(current_place)
                travel_points += len(current_place)
            current_place = ""
            store = False
            valid = False
        if not store:
            if ch == "=":
                validator = "="
                store = True
            elif ch == "/":
                validator = "/"
                store = True
    if store and ch != "=" and ch != "/":
        current_place += ch
print(f"Destinations: {', '.join(valid_places)}")

print(f"Travel Points: {travel_points}")

