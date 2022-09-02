number = float(input())
is_between = False
while not is_between:
    if 1 <= number <= 100:
        is_between = True
        print(f"The number {number} is between 1 and 100")
    else:
        number = float(input())