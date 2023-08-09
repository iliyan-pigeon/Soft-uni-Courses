from django.shortcuts import render, redirect
from djangoRegularExam.fruitipedia.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from djangoRegularExam.fruitipedia.models import Profile, Fruit


def profile_validator():
    try:
        return Profile.objects.first()

    except Profile.DoesNotExist:
        return None


def index_page(request):
    profile = profile_validator()

    context = {
        'profile': profile
    }

    return render(request, 'core/index.html', context)


def dashboard_page(request):
    profile = profile_validator()
    fruits = Fruit.objects.all()

    context = {
        'profile': profile,
        'fruits': fruits,
    }

    return render(request, 'core/dashboard.html', context)


def fruit_create_page(request):
    profile = profile_validator()

    if request.method == "GET":
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'fruit/create-fruit.html', context)


def fruit_details_page(request, pk):
    profile = profile_validator()
    fruit = Fruit.objects.get(pk=pk)

    context = {
        'profile': profile,
        'fruit': fruit
    }

    return render(request, 'fruit/details-fruit.html', context)


def fruit_edit_page(request, pk):
    profile = profile_validator()
    fruit = Fruit.objects.get(pk=pk)

    if request.method == "GET":
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'profile': profile,
        'fruit': fruit,
    }

    return render(request, 'fruit/edit-fruit.html', context)


def fruit_delete_page(request, pk):
    profile = profile_validator()
    fruit = Fruit.objects.get(pk=pk)

    if request.method == "GET":
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)
        fruit.delete()
        return redirect('dashboard page')

    context = {
        'form': form,
        'profile': profile,
        'fruit': fruit,
    }

    return render(request, 'fruit/delete-fruit.html', context)


def profile_create_page(request):
    profile = profile_validator()

    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/create-profile.html', context)


def profile_details_page(request):
    profile = profile_validator()
    fruits_length = len(Fruit.objects.all())
    full_name = f"{profile.first_name} {profile.last_name}"

    context = {
        'profile': profile,
        'full_name': full_name,
        'fruits_length': fruits_length,
    }

    return render(request, 'profile/details-profile.html', context)


def profile_edit_page(request):
    profile = profile_validator()

    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details page')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/edit-profile.html', context)


def profile_delete_page(request):
    profile = profile_validator()
    fruits = Fruit.objects.all()

    if request.method == "GET":
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        profile.delete()
        fruits.delete()
        return redirect('index page')

    context = {
        'form': form,
        'profile': profile,
        'fruits': fruits,
    }

    return render(request, 'profile/delete-profile.html', context)
