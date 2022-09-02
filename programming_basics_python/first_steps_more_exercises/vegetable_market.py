price_kilo_vegetables = float(input())
price_kilo_fruits = float(input())
kilo_vegetables = int(input())
kilo_fruits = int(input())
total_value_vegetables = price_kilo_vegetables * kilo_vegetables
total_value_fruits = price_kilo_fruits * kilo_fruits
total_value_lv = total_value_vegetables + total_value_fruits
eu_course = 1.94
total_value_eu = total_value_lv / eu_course
print(f'{total_value_eu:.2f}')