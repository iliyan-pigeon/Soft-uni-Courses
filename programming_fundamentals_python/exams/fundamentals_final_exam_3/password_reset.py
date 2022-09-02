password = input()
command = input()
while command != "Done":
    command = command.split()
    the_command = command[0]
    if the_command == "TakeOdd":
        new_password = ""
        for i in range(len(password)):
            if i % 2 != 0:
                new_password += password[i]
        password = new_password
        print(password)
    elif the_command == "Cut":
        index = int(command[1])
        length = int(command[2])
        password = password.replace(password[index:index+length], "", 1)
        print(password)
    elif the_command == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        elif substring not in password:
            print("Nothing to replace!")
    command = input()
print(f"Your password is: {password}")
