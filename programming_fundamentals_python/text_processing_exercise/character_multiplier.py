strings = input().split()
first_string = strings[0]
second_string = strings[1]
result = 0
if len(first_string) > len(second_string):
    for i in range(len(second_string)):
        result += ord(first_string[i]) * ord(second_string[i])
    for j in range(len(second_string), len(first_string)):
        result += ord(first_string[j])
elif len(first_string) < len(second_string):
    for i in range(len(first_string)):
        result += ord(first_string[i]) * ord(second_string[i])
    for j in range(len(first_string), len(second_string)):
        result += ord(second_string[j])
elif len(first_string) == len(second_string):
    for i in range(len(first_string)):
        result += ord(first_string[i]) * ord(second_string[i])
print(result)
