fruit = input()
day = input()
amount = float(input())
is_valid = True
price = 0
if fruit == "banana":
    if day == "Monday" or day == "Tuesday " or day == "Wednesday" \
        or day == "Thursday" or day == "Friday":
        price = 2.5
    elif day == "Saturday" or day == "Sunday":
        price = 2.7
    else:
        is_valid = False
elif fruit == "apple":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" \
        or day == "Thursday" or day == "Friday":
        price = 1.2
    elif day == "Saturday" or day == "Sunday":
        price = 1.25
    else:
        is_valid = False
elif fruit == "orange":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" \
        or day == "Thursday" or day == "Friday":
        price = 0.85
    elif day == "Saturday" or day == "Sunday":
        price = 0.9
    else:
        is_valid = False
elif fruit == "grapefruit":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" \
        or day == "Thursday" or day == "Friday":
        price = 1.45
    elif day == "Saturday" or day == "Sunday":
        price = 1.60
    else:
        is_valid = False
elif fruit == "kiwi":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" \
        or day == "Thursday" or day == "Friday":
        price = 2.7
    elif day == "Saturday" or day == "Sunday":
        price = 3.00
    else:
        is_valid = False
elif fruit == "pineapple":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" \
        or day == "Thursday" or day == "Friday":
        price = 5.5
    elif day == "Saturday" or day == "Sunday":
        price = 5.6
    else:
        is_valid = False
elif fruit == "grapes":
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" \
        or day == "Thursday" or day == "Friday":
        price = 3.85
    elif day == "Saturday" or day == "Sunday":
        price = 4.2
    else:
        is_valid = False
else:
    is_valid = False
if is_valid:
    total_price = amount * price
    print(f"{total_price:.2f}")
else:
    print("error")
