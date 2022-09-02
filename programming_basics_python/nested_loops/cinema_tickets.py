name_of_film = input()
total_tickets = 0
standard_tickets = 0
student_tickets = 0
kid_tickets = 0
percent_standard = 0
percent_student = 0
percent_kid = 0
while name_of_film != "Finish":
    free_places = int(input())
    tickets_for_movie = 0
    percent_fullness = 0
    type_of_ticket = input()
    while type_of_ticket != "End" and tickets_for_movie < free_places:
        if type_of_ticket == "standard":
            standard_tickets += 1
            tickets_for_movie += 1
            total_tickets += 1
        elif type_of_ticket == "student":
            student_tickets += 1
            tickets_for_movie += 1
            total_tickets += 1
        elif type_of_ticket == "kid":
            kid_tickets += 1
            tickets_for_movie += 1
            total_tickets += 1
        if tickets_for_movie < free_places:
            type_of_ticket = input()
    percent_fullness = tickets_for_movie / free_places * 100
    print(f"{name_of_film} - {percent_fullness:.2f}% full.")
    name_of_film = input()
percent_standard = standard_tickets / total_tickets * 100
percent_student = student_tickets / total_tickets * 100
percent_kid = kid_tickets / total_tickets * 100
print(f"Total tickets: {total_tickets}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")