numbers = [int(number) for number in input().split(", ")]
boundary = 10
while len(numbers) != 0:
    current_group = [number for number in numbers if number <= boundary]
    print(f"Group of {boundary}'s: {current_group}")
    for number in current_group:
        numbers.remove(number)
    boundary += 10
