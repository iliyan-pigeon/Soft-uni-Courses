control_minutes = int(input())
control_seconds = int(input())
furrow_length_metres = float(input())
seconds_for_one_hundred_metres = int(input())
control_in_seconds = control_minutes * 60 + control_seconds
control_time = furrow_length_metres / 100 * seconds_for_one_hundred_metres
bonus_acceleration = furrow_length_metres / 120 * 2.5
final_time = control_time - bonus_acceleration
if final_time <= control_in_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {final_time:.3f}.")
else:
    difference = abs(final_time - control_in_seconds)
    print(f"No, Marin failed! He was {difference:.3f} second slower.")

