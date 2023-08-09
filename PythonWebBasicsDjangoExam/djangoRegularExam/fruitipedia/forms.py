from django import forms
from djangoRegularExam.fruitipedia.models import Profile, Fruit


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = False
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(render_value=True, attrs={'placeholder': 'Password'}),
        }


class FruitCreateForm(forms.ModelForm):

    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description', 'nutrition']
        labels = False
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.TextInput(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.TextInput(attrs={'placeholder': 'Nutrition Info'}),
        }


class FruitEditForm(forms.ModelForm):

    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description', 'nutrition']
        labels = {
            'name': 'Name:',
            'image_url': 'Image URL:',
            'description': 'Description:',
            'nutrition': 'Nutrition:',
        }


class FruitDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = Fruit
        fields = '__all__'


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image_url', 'age']
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'image_url': 'Image URL:',
            'age': 'Age:',
        }


class ProfileDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = Profile
        fields = '__all__'
