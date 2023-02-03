from collections import deque

pizzas_queue = deque(int(i) for i in input().split(", "))
workers_stack = [int(i) for i in input().split(", ")]

total_pizza_made = 0
orders_completed = False

while True:
    if not pizzas_queue:
        orders_completed = True
        break
    elif not workers_stack:
        break

    current_order = pizzas_queue.popleft()
    if current_order <= 0 or current_order > 10:
        continue
    current_worker = workers_stack.pop()

    if current_order <= current_worker:
        total_pizza_made += current_order
    elif current_order > current_worker:
        difference = abs(current_worker - current_order)
        total_pizza_made += current_worker
        pizzas_queue.appendleft(difference)

if orders_completed:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza_made}")
    print(f"Employees: {', '.join(map(str, workers_stack))}")
elif not orders_completed:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizzas_queue))}")


