import sys

number = int(input())
biggest_number = -sys.maxsize
all_numbers = 0
other_numbers = 0
difference = 0
for i in range(number):
    value = int(input())
    all_numbers += value
    if value > biggest_number:
        biggest_number = value
    other_numbers = all_numbers - biggest_number
if biggest_number == other_numbers:
    print("Yes")
    print(f"Sum = {biggest_number}")
else:
    difference = abs(biggest_number - other_numbers)
    print("No")
    print(f"Diff = {difference}")

 #   number = int(input())
  #  biggest_number = ""
  #  all_numbers = 0
  #  other_numbers = 0
  #  difference = 0
  #  for i in range(number):
   #     value = int(input())
   #     all_numbers += value
   #     if i == 0:
   #         biggest_number = value
  #      if value > biggest_number:
  #          biggest_number = value
  #      other_numbers = all_numbers - biggest_number
   # if biggest_number == other_numbers:
  #      print("Yes")
  #      print(f"Sum = {biggest_number}")
  #  else:
   #     difference = abs(biggest_number - other_numbers)
   #     print("No")
  #      print(f"Diff = {difference}")