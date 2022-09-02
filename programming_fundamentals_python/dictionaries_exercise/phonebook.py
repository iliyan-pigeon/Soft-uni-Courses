person_info = input()
phonebook = {}
while "-" in person_info:
    person_info = person_info.split("-")
    person = person_info[0]
    number = person_info[1]
    if person not in phonebook:
        phonebook[person] = ""
    phonebook[person] = number
    person_info = input()
peoples_data = int(person_info)
for i in range(peoples_data):
    person = input()
    if person in phonebook:
        print(f"{person} -> {phonebook[person]}")
    elif person not in phonebook:
        print(f"Contact {person} does not exist.")

