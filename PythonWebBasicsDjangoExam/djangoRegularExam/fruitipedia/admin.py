from django.contrib import admin
from djangoRegularExam.fruitipedia.models import Profile, Fruit


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    pass


@admin.register(Fruit)
class Fruit(admin.ModelAdmin):
    pass
