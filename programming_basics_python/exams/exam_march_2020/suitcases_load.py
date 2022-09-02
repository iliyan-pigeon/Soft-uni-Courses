trunk_capacity = float(input())
suitcase_volume = input()
suitcases_number = 0
space_taken = 0
no_space = False
suitcase_counter = 0
while suitcase_volume != "End":
    volume_suitcase = float(suitcase_volume)
    suitcase_counter += 1
    if suitcase_counter == 3:
        volume_suitcase += (volume_suitcase * 0.1)
        suitcase_counter = 0
    if space_taken + volume_suitcase > trunk_capacity:
        no_space = True
        break
    space_taken += volume_suitcase
    suitcases_number += 1
    suitcase_volume = input()
if not no_space:
    print("Congratulations! All suitcases are loaded!")
elif no_space:
    print("No more space!")
print(f"Statistic: {suitcases_number} suitcases loaded.")