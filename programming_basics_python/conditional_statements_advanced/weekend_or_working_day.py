day = input()
working_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" \
    or day == "Thursday" or day == "Friday"
weekend = day == "Saturday" or day == "Sunday"
if working_day:
    print("Working day")
elif weekend:
    print("Weekend")
else:
    print("Error")