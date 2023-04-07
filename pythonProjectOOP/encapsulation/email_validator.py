class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        name_valid = len(name) >= self.min_length
        return name_valid

    def __is_mail_valid(self, mail):
        mail_valid = mail in self.mails
        return mail_valid

    def __is_domain_valid(self, domain):
        domain_valid = domain in self.domains
        return domain_valid

    def validate(self, email):
        email = email.split("@")
        email_name = email[0]
        email_mail, email_domain = email[1].split(".")

        return self.__is_name_valid(email_name) and self.__is_mail_valid(email_mail) and self.__is_domain_valid(email_domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))