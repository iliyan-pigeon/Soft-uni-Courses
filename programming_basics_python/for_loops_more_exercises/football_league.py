stadium_capacity = int(input())
number_of_fans = int(input())
number_fans_sector_a = 0
number_fans_sector_b = 0
number_fans_sector_v = 0
number_fans_sector_g = 0
percent_sector_a = 0
percent_sector_b = 0
percent_sector_v = 0
percent_sector_g = 0
percent_all_fans = 0
percent_total_fans = 0
for fan in range(number_of_fans):
    current_fan = input()
    if current_fan == "A":
        number_fans_sector_a += 1
    elif current_fan == "B":
        number_fans_sector_b += 1
    elif current_fan == "V":
        number_fans_sector_v += 1
    elif current_fan == "G":
        number_fans_sector_g += 1
percent_sector_a = number_fans_sector_a / number_of_fans * 100
percent_sector_b = number_fans_sector_b / number_of_fans * 100
percent_sector_v = number_fans_sector_v / number_of_fans * 100
percent_sector_g = number_fans_sector_g / number_of_fans * 100
percent_total_fans = number_of_fans / stadium_capacity * 100
print(f"{percent_sector_a:.2f}%")
print(f"{percent_sector_b:.2f}%")
print(f"{percent_sector_v:.2f}%")
print(f"{percent_sector_g:.2f}%")
print(f"{percent_total_fans:.2f}%")
