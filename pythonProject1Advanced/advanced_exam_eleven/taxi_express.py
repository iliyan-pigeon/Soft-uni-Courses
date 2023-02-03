from collections import deque

customers = deque(int(i) for i in input().split(", "))
drivers = deque(int(i) for i in input().split(", "))

total_time_driving = 0

while customers and drivers:
    current_customer = customers.popleft()
    current_driver = drivers.pop()

    if current_customer <= current_driver:
        total_time_driving += current_customer
    else:
        customers.appendleft(current_customer)

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time_driving} minutes")
else:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(map(str, customers))}")