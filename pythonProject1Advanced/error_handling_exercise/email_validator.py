from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


pattern = r"([A-z]+)\@[A-z]+(\.[a-z]+)"
valid_domains = [".com", ".net", ".bg", ".org"]
email = input()

while email != "End":
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    email_components = findall(pattern, email)
    email_name = email_components[0][0]
    domain = email_components[0][1]
    if len(email_name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")
    email = input()
