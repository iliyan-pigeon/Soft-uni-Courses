period_of_time = int(input())
examined_patients = 0
unexamined_patients = 0
doctors = 7
difference = 0
for day in range(1, period_of_time + 1):
    if day % 3 == 0:
        if examined_patients < unexamined_patients:
            doctors += 1
    patients_per_day = int(input())
    if patients_per_day <= doctors:
        examined_patients += patients_per_day
    elif patients_per_day > doctors:
        difference = abs(patients_per_day - doctors)
        examined_patients += doctors
        unexamined_patients += difference
print(f"Treated patients: {examined_patients}.")
print(f"Untreated patients: {unexamined_patients}.")
