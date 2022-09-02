numbers = [int(number) for number in input().split()]
numbers_to_remove = int(input())
for i in range(numbers_to_remove):
    numbers.remove(min(numbers))
final_string = ", ".join(map(str, numbers))
print(final_string)


