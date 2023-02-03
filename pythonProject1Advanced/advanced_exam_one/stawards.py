from collections import deque

seats = input().split(", ")
first_numbers = deque(int(i) for i in input().split(", "))
second_numbers = deque([int(i) for i in input().split(", ")])

rotations_amount = 0
taken_seats = []

while rotations_amount < 10 and len(taken_seats) < 3:
    first_number = first_numbers.popleft()
    second_number = second_numbers.pop()
    character = chr(first_number + second_number)
    first_seat = f"{first_number}{character}"
    second_seat = f"{second_number}{character}"

    if first_seat in seats:
        if first_seat not in taken_seats:
            taken_seats.append(first_seat)
    elif second_seat in seats:
        if second_seat not in taken_seats:
            taken_seats.append(second_seat)
    else:
        first_numbers.append(first_number)
        second_numbers.appendleft(second_number)

    rotations_amount += 1

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations_amount}")
