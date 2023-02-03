from collections import deque

prepared_food_amount = int(input())
orders_queue = deque(int(i) for i in input().split())
print(max(orders_queue))
while orders_queue:
    if orders_queue[0] <= prepared_food_amount:
        prepared_food_amount -= orders_queue.popleft()
    else:
        break
if orders_queue:
    print("Orders left:", end=" ")
    for order in orders_queue:
        print(order, end=" ")
else:
    print("Orders complete")
