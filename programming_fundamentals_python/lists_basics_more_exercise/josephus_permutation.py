people = input().split()
through_number = int(input())
killed_list = []
counter = 0
index = 0
while len(people) != 0:
    counter += 1
    if counter == through_number:
        killed_list.append(people.pop(index))
        counter = 0
    else:
        index += 1
    if index >= len(people):
        index = 0
killed_string = ",".join(killed_list)
print(f"[{killed_string}]")
