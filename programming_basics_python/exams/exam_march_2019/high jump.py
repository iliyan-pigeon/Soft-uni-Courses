needed_height = int(input())
is_successful = False
lath_height = needed_height - 30
attempts = 0
current_attempts = 0
while not is_successful:
    current_jump_height = int(input())
    attempts += 1
    if needed_height <= lath_height < current_jump_height:
        is_successful = True
        continue
    if current_jump_height > lath_height:
        lath_height += 5
        current_attempts = 0
    elif current_jump_height <= lath_height:
        current_attempts += 1
    if current_attempts == 3:
        break
if not is_successful:
    print(f"Tihomir failed at {lath_height}cm after {attempts} jumps.")
elif is_successful:
    print(f"Tihomir succeeded, he jumped over {lath_height}cm after {attempts} jumps.")