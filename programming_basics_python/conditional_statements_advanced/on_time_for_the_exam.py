hour_of_beginning = int(input())
minutes_of_beginning = int(input())
hour_of_arriving = int(input())
minutes_of_arriving = int(input())
beginning_in_minutes = hour_of_beginning * 60 + minutes_of_beginning
arriving_in_minutes = hour_of_arriving * 60 + minutes_of_arriving
if arriving_in_minutes <= beginning_in_minutes and \
    arriving_in_minutes >= beginning_in_minutes - 30:
    print("On time")
elif arriving_in_minutes < beginning_in_minutes - 30:
    print("Early")
elif arriving_in_minutes > beginning_in_minutes:
    print("Late")
difference = abs(beginning_in_minutes - arriving_in_minutes)
hour = difference // 60
minutes = difference % 60
if arriving_in_minutes > beginning_in_minutes - 60 and arriving_in_minutes <= beginning_in_minutes:
    print(f"{minutes} minutes before the start")
elif arriving_in_minutes <= beginning_in_minutes - 60:
    print(f"{hour}:{minutes:02d} hours before the start")
elif arriving_in_minutes < beginning_in_minutes + 60:
    print(f"{minutes} minutes after the start")
elif arriving_in_minutes >= beginning_in_minutes + 60:
    print(f"{hour}:{minutes:02d} hours after the start")




