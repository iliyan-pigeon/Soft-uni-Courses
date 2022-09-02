def calculate(a, b, operator):
    output = 0
    if operator == "multiply":
        output = a * b
    elif operator == "divide":
        output = a / b
    elif operator == "add":
        output = a + b
    elif operator == "subtract":
        output = a - b
    return int(output)


input_operator = input()
first_number = int(input())
second_number = int(input())
result = calculate(first_number, second_number, input_operator)
print(result)