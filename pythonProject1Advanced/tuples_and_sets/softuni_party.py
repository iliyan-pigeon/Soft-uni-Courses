guests_number = int(input())
guest_list = set()
arrived_guests = set()
for guest in range(guests_number):
    current_guest = input()
    guest_list.add(current_guest)
arriving_guest = input()
while arriving_guest != "END":
    arrived_guests.add(arriving_guest)
    arriving_guest = input()
missing_guests = guest_list - arrived_guests
print(len(missing_guests))
for guest in sorted(missing_guests):
    print(guest)

