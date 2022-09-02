season = input()
kilometres_per_month = float(input())
tax_percent = 0.1
gross_salary = 0
net_salary = 0
price_per_kilometres = 0
if kilometres_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_kilometres = 0.75
    elif season == "Summer":
        price_per_kilometres = 0.9
    elif season == "Winter":
        price_per_kilometres = 1.05
elif kilometres_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_kilometres = 0.95
    elif season == "Summer":
        price_per_kilometres = 1.1
    elif season == "Winter":
        price_per_kilometres = 1.25
elif kilometres_per_month <= 20000:
    price_per_kilometres = 1.45
total_distance = kilometres_per_month * 4
gross_salary = total_distance * price_per_kilometres
tax_amount = gross_salary * 0.1
net_salary = gross_salary - tax_amount
print(f"{net_salary:.2f}")
