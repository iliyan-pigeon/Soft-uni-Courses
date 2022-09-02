groups_of_climbers = int(input())
total_climbers = 0
musala_climbers = 0
mont_blanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
percent_musala = 0
percent_mont_blanc = 0
percent_kilimanjaro = 0
percent_k2 = 0
percent_everest = 0
for group in range(groups_of_climbers):
    people_in_group = int(input())
    if people_in_group <= 5:
        musala_climbers += people_in_group
    elif people_in_group <= 12:
        mont_blanc_climbers += people_in_group
    elif people_in_group <= 25:
        kilimanjaro_climbers += people_in_group
    elif people_in_group <= 40:
        k2_climbers += people_in_group
    elif people_in_group > 40:
        everest_climbers += people_in_group
total_climbers = musala_climbers + mont_blanc_climbers + kilimanjaro_climbers \
+ k2_climbers + everest_climbers
percent_musala = musala_climbers / total_climbers * 100
percent_mont_blanc = mont_blanc_climbers / total_climbers * 100
percent_kilimanjaro = kilimanjaro_climbers / total_climbers * 100
percent_k2 = k2_climbers / total_climbers * 100
percent_everest = everest_climbers / total_climbers * 100
print(f"{percent_musala:.2f}%")
print(f"{percent_mont_blanc:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")
