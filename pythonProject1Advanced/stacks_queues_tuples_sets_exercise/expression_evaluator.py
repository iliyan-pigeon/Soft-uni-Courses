from collections import deque
from math import floor

sequence_to_evaluate = input().split()
result = 0
numbers_queue = deque()
for ch in sequence_to_evaluate:
    if ch.lstrip("-").isdigit():
        numbers_queue.append(int(ch))
    elif ch == "*":
        while numbers_queue:
            result = numbers_queue.popleft() * numbers_queue.popleft()
            if len(numbers_queue) == 1:
                result = result * numbers_queue.popleft()
        numbers_queue.append(result)
    elif ch == "/":
        while numbers_queue:
            result = floor(numbers_queue.popleft() / numbers_queue.popleft())
            if len(numbers_queue) == 1:
                result = floor(result / numbers_queue.popleft())
        numbers_queue.append(floor(result))
    elif ch == "+":
        while numbers_queue:
            result = numbers_queue.popleft() + numbers_queue.popleft()
            if len(numbers_queue) == 1:
                result = result + numbers_queue.popleft()
        numbers_queue.append(result)
    elif ch == "-":
        while numbers_queue:
            result = numbers_queue.popleft() - numbers_queue.popleft()
            if len(numbers_queue) == 1:
                result = result - numbers_queue.popleft()
        numbers_queue.append(result)
print(result)

