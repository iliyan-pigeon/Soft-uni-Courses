import re

furniture_info = input()
furniture_names = []
total_price = 0
pattern = r">>([a-zA-Z]+)<<([0-9]+[\.0-9]*)!([0-9]+)"
while furniture_info != "Purchase":
    matches = re.findall(pattern, furniture_info)
    if matches:
        furniture_name = matches[0][0]
        furniture_price = float(matches[0][1])
        furniture_quantity = int(matches[0][2])
        current_total_price = furniture_price * furniture_quantity
        furniture_names.append(furniture_name)
        total_price += current_total_price
    furniture_info = input()
print("Bought furniture:")
for name in furniture_names:
    print(name)
print(f"Total money spend: {total_price:.2f}")
