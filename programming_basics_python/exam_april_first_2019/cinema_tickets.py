film_name = input()
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
percent_student = 0
percent_standard = 0
percent_kid = 0
while film_name != "Finish":
    free_places = int(input())
    ticket_type = input()
    current_tickets = 0
    percent_full = 0
    while ticket_type != "End":
        current_tickets += 1
        total_tickets += 1
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        if current_tickets == free_places:
            break
        ticket_type = input()
    percent_full = current_tickets / free_places * 100
    print(f"{film_name} - {percent_full:.2f}% full.")
    film_name = input()
percent_student = student_tickets / total_tickets * 100
percent_standard = standard_tickets / total_tickets * 100
percent_kid = kid_tickets / total_tickets * 100
print(f"Total tickets: {total_tickets}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")
