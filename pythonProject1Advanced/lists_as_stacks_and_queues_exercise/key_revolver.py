from collections import deque

single_bullet_price = int(input())
gun_barrel_size = int(input())
bullets_stack = [int(i) for i in input().split()]
locks_queue = deque(int(i) for i in input().split())
intelligence_value = int(input())
gun_barrel_counter = 0
used_bullets_counter = 0
get_through = True
while locks_queue:
    if bullets_stack:
        current_bullet = bullets_stack.pop()
        used_bullets_counter += 1
        gun_barrel_counter += 1
        if current_bullet <= locks_queue[0]:
            locks_queue.popleft()
            print("Bang!")
        elif current_bullet > locks_queue[0]:
            print("Ping!")
        if gun_barrel_counter == gun_barrel_size and bullets_stack:
            print("Reloading!")
            gun_barrel_counter = 0
    elif not bullets_stack:
        get_through = False
        break
if get_through:
    bullets_price = single_bullet_price * used_bullets_counter
    profit = intelligence_value - bullets_price
    print(f"{len(bullets_stack)} bullets left. Earned ${profit}")
elif not get_through:
    print(f"Couldn't get through. Locks left: {len(locks_queue)}")
