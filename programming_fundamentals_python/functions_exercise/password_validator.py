def password_validator(password):
    good_password = True
    digit_counter = 0
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        good_password = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        good_password = False
    for character in password:
        if character.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        good_password = False
    if good_password:
        print("Password is valid")


the_password = input()
password_validator(the_password)
