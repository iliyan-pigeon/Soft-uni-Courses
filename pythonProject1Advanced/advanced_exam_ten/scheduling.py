from collections import deque

jobs = deque(int(i) for i in input().split(", "))
index_searched_job = int(input())
clock_cycles = 0

for i in range(jobs[index_searched_job] + 1):
    while i in jobs:
        clock_cycles += i
        jobs.remove(i)

print(clock_cycles)
