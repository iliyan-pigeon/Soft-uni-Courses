number_of_months = int(input())
average_monthly_expense = 0
all_expenses = 0
total_electricity = 0
total_water = 0
total_internet = 0
total_others = 0
water_per_month = 20
internet_per_month = 15
others_per_month = 0
for month in range(number_of_months):
    current_electricity = float(input())
    total_electricity += current_electricity
    total_water += water_per_month
    total_internet += internet_per_month
    total_others += (current_electricity + water_per_month + internet_per_month) +\
    ((current_electricity + water_per_month + internet_per_month) * 0.2)
all_expenses = total_electricity + total_water + total_internet + total_others
average_monthly_expense = all_expenses / number_of_months
print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_others:.2f} lv")
print(f"Average: {average_monthly_expense:.2f} lv")