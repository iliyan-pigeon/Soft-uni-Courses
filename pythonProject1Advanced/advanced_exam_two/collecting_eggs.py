from collections import deque

eggs = deque(int(i) for i in input().split(", "))
papers = deque(int(i) for i in input().split(", "))

filled_boxes = 0
box_size = 50

while eggs and papers:
    current_egg = eggs.popleft()
    if current_egg == 13:
        transmitter = papers.pop()
        papers.append(papers.popleft())
        papers.appendleft(transmitter)
    elif current_egg > 0:
        current_paper = papers.pop()
        current_sum = current_egg + current_paper
        if current_sum <= box_size:
            filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")
elif papers:
    print(f"Pieces of paper left: {', '.join(map(str, papers))}")