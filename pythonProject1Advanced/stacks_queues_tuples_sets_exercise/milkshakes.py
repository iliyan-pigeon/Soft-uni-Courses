from collections import deque

chocolates_stack = [int(i) for i in input().split(", ")]
milk_cups_queue = deque(int(i) for i in input().split(", "))
milkshakes_amount = 0
while milkshakes_amount < 5 and chocolates_stack and milk_cups_queue:
    flag = False
    if chocolates_stack[-1] <= 0:
        chocolates_stack.pop()
        flag = True
    if milk_cups_queue[0] <= 0:
        milk_cups_queue.popleft()
        flag = True
    if flag:
        continue
    if chocolates_stack[-1] == milk_cups_queue[0]:
        chocolates_stack.pop()
        milk_cups_queue.popleft()
        milkshakes_amount += 1
    else:
        milk_cups_queue.append(milk_cups_queue.popleft())
        chocolates_stack.append(chocolates_stack.pop() - 5)
if milkshakes_amount == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates_stack:
    print(f"Chocolate: {', '.join(str(i) for i in chocolates_stack)}")
else:
    print("Chocolate: empty")
if milk_cups_queue:
    print(f"Milk: {', '.join(str(i) for i in milk_cups_queue)}")
else:
    print("Milk: empty")
