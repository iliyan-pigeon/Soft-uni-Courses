from django.core import validators
from django.db import models
from .validators import starts_with_letter_validator, only_letters_validator


class Profile(models.Model):

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=25,
        validators=(
            validators.MinLengthValidator(2),
            starts_with_letter_validator,
        ),
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=35,
        validators=(
            validators.MinLengthValidator(1),
            starts_with_letter_validator,
        ),
    )

    email = models.EmailField(
        null=False,
        blank=False,
        max_length=40,
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(
            validators.MinLengthValidator(8),
        ),
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        default=18,
    )


class Fruit(models.Model):

    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
            only_letters_validator,
        ),
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )
