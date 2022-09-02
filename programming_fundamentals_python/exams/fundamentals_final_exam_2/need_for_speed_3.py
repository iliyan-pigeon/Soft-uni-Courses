cars_number = int(input())
cars = {}
for i in range(cars_number):
    car = input().split("|")
    the_car = car[0]
    mileage = int(car[1])
    fuel = int(car[2])
    cars[the_car] = {}
    cars[the_car]["mileage"] = mileage
    cars[the_car]["fuel"] = fuel
command = input()
while command != "Stop":
    command = command.split(" : ")
    the_command = command[0]
    if the_command == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        elif cars[car]["fuel"] >= fuel:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]["mileage"] >= 100000:
                del cars[car]
                print(f"Time to sell the {car}!")
    elif the_command == "Refuel":
        car = command[1]
        fuel = int(command[2])
        if cars[car]["fuel"] + fuel > 75:
            fuel = 75 - cars[car]["fuel"]
        cars[car]["fuel"] += fuel
        print(f"{car} refueled with {fuel} liters")
    elif the_command == "Revert":
        car = command[1]
        kilometers = int(command[2])
        if cars[car]["mileage"] - kilometers < 10000:
            cars[car]["mileage"] = 10000
        else:
            cars[car]["mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input()
for car in cars:
    mileage = cars[car]["mileage"]
    fuel = cars[car]["fuel"]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")

