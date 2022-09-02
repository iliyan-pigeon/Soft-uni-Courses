import re

total_income = 0
pattern = r"\%([A-Z][a-z]+)\%[^\%\$\|\.]*?\<(.+)\>[^\%\$\|\.]*?\|([0-9]+)\|[^\%\$\|\.]*?([0-9]+\.?[0-9]+?)\$"
command = input()
while command != "end of shift":
    match = re.findall(pattern, command)
    if match:
        customer = match[0][0]
        product = match[0][1]
        count = int(match[0][2])
        price = float(match[0][3])
        total_price = count * price
        total_income += total_price
        print(f"{customer}: {product} - {total_price:.2f}")
    command = input()

print(f"Total income: {total_income:.2f}")

