stack = []
queries_amount = int(input())
for query in range(queries_amount):
    current_query = input()
    if "1" in current_query:
        number = int(current_query.split()[1])
        stack.append(number)
    elif "2" in current_query:
        if stack:
            stack.pop()
    elif "3" in current_query:
        if stack:
            print(max(stack))
    elif "4" in current_query:
        if stack:
            print(min(stack))
while stack:
    if len(stack) == 1:
        print(stack.pop())
    else:
        print(stack.pop(), end=", ")
