from django.core.exceptions import ValidationError



def starts_with_letter_validator(value):
    if not value[0].isalpha():
        raise ValidationError('Your name must start with a letter!')


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError('Fruit name should contain only letters!')



