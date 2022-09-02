groups_number = int(input())
total_people = 0
musala_people = 0
mont_blanc_people = 0
kilimanjaro_people = 0
k2_people = 0
everest_people = 0
percent_musala = 0
percent_mont_blanc = 0
percent_kilimanjaro = 0
percent_k2 = 0
percent_everest = 0
for group in range(groups_number):
    current_people = int(input())
    if current_people <= 5:
        musala_people += current_people
    elif current_people <= 12:
        mont_blanc_people += current_people
    elif current_people <= 25:
        kilimanjaro_people += current_people
    elif current_people <= 40:
        k2_people += current_people
    elif current_people > 40:
        everest_people += current_people
total_people = musala_people + mont_blanc_people + kilimanjaro_people\
    + k2_people + everest_people
percent_musala = musala_people / total_people * 100
percent_mont_blanc = mont_blanc_people / total_people * 100
percent_kilimanjaro = kilimanjaro_people / total_people * 100
percent_k2 = k2_people / total_people * 100
percent_everest = everest_people / total_people * 100
print(f"{percent_musala:.2f}%")
print(f"{percent_mont_blanc:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")