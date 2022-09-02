record_in_seconds = float(input())
range_in_metres = float(input())
seconds_per_metre = float(input())
time_to_finish = range_in_metres * seconds_per_metre
delay = (range_in_metres // 15) * 12.5
final_time = time_to_finish + delay
if final_time < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {final_time:.2f} seconds.')
elif final_time >= record_in_seconds:
    seconds_slower = final_time - record_in_seconds
    print(f'No, he failed! He was {seconds_slower:.2f} seconds slower.')