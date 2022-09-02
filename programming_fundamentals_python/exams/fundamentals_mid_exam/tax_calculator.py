vehicles_to_tax = input().split(">>")
total_revenue = 0
for vehicle in vehicles_to_tax:
    valid_vehicle = True
    total_tax = 0
    vehicle = vehicle.split()
    car_type = vehicle[0]
    years_to_pay = int(vehicle[1])
    traveled_kilometres = int(vehicle[2])
    if car_type == "family":
        initial_tax = 50
        amount_decline = 5
        tax_increase = 12
        total_tax = traveled_kilometres // 3000 * tax_increase + (initial_tax - years_to_pay * amount_decline)
    elif car_type == "heavyDuty":
        initial_tax = 80
        amount_decline = 8
        tax_increase = 14
        total_tax = traveled_kilometres // 9000 * tax_increase + (initial_tax - years_to_pay * amount_decline)
    elif car_type == "sports":
        initial_tax = 100
        amount_decline = 9
        tax_increase = 18
        total_tax = traveled_kilometres // 2000 * tax_increase + (initial_tax - years_to_pay * amount_decline)
    else:
        print("Invalid car type.")
        valid_vehicle = False
    if valid_vehicle:
        print(f"A {car_type} car will pay {total_tax:.2f} euros in taxes.")
        total_revenue += total_tax
print(f"The National Revenue Agency will collect {total_revenue:.2f} euros in taxes.")
