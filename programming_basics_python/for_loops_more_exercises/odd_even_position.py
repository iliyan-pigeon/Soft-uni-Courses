import sys

number_of_numbers = int(input())
odd_total = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_total = 0
even_min = sys.maxsize
even_max = -sys.maxsize
for i in range(1, number_of_numbers + 1):
    number = float(input())
    if i % 2 != 0:
        odd_total += number
        if odd_min > number:
            odd_min = number
        if odd_max < number:
            odd_max = number
    elif i % 2 == 0:
        even_total += number
        if even_min > number:
            even_min = number
        if even_max < number:
            even_max = number
if number_of_numbers == 1:
    print(f"OddSum={odd_total:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_total:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
elif number_of_numbers > 1:
    print(f"OddSum={odd_total:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_total:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
elif number_of_numbers == 0:
   print()