visitors_number = int(input())
number_training_people = 0
number_protein_people = 0
number_back = 0
number_chest = 0
number_legs = 0
number_abs = 0
number_protein_shake = 0
number_protein_bar = 0
percent_training = 0
percent_protein = 0
for visitor in range(visitors_number):
    activity = input()
    if activity == "Back":
        number_back += 1
    elif activity == "Chest":
        number_chest += 1
    elif activity == "Legs":
        number_legs += 1
    elif activity == "Abs":
        number_abs += 1
    elif activity == "Protein shake":
        number_protein_shake += 1
    elif activity == "Protein bar":
        number_protein_bar += 1
number_training_people = number_back + number_chest\
    + number_legs + number_abs
number_protein_people = number_protein_shake + number_protein_bar
percent_training = number_training_people / visitors_number * 100
percent_protein = number_protein_people / visitors_number * 100
print(f"{number_back} - back")
print(f"{number_chest} - chest")
print(f"{number_legs} - legs")
print(f"{number_abs} - abs")
print(f"{number_protein_shake} - protein shake")
print(f"{number_protein_bar} - protein bar")
print(f"{percent_training:.2f}% - work out")
print(f"{percent_protein:.2f}% - protein")