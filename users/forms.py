# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile

class CustomSignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, label='Полное имя')
    address = forms.CharField(max_length=200, required=True, label='Адресс')
    date_of_birth = forms.DateField(
        required=False,
        input_formats=['%d.%m.%Y'],  # Specify the input format here
        help_text='Enter the date in the format DD.MM.YYYY', label='Дата рождения'
    )

    email = forms.EmailField(required=True, label='Электронная почта')


    class Meta:
        model = UserProfile
        fields = ['email', 'full_name', 'address', 'date_of_birth', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'email', 'address', 'date_of_birth']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
        }


class LoginForm(AuthenticationForm):
    email = forms.EmailField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'email',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))

    class Meta:
        model = UserProfile
        fields = ['email', 'password', 'remember_me']



