time_first = int(input())
time_second = int(input())
time_third = int(input())
time_combined = time_first + time_second + time_third
minutes = time_combined // 60
seconds = time_combined % 60
if seconds < 10:
    print(f'{minutes}:0{seconds} ')
else:
    print(f'{minutes}:{seconds}')
    