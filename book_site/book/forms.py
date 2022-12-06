from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core import validators

from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import *


class ReviewsForm(forms.ModelForm):
    """ Форма для добавления отзывов """

    captcha = ReCaptchaField()

    class Meta:
        model = Reviews

        fields = ("name", "email", "text", "captcha")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border"}),
            "email": forms.EmailInput(attrs={"class": "form-control border"}),
            "text": forms.TextInput(attrs={"class": "form-control border"})
        }


class UserRegisterForm(UserCreationForm):
    """ Форма для регистрации пользователя """

    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User

        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    """ Форма для авторизации пользователя """

    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SuggestBookForm(forms.ModelForm):
    captcha = ReCaptchaField()
    user_book = forms.FileField(label='Книга пользователя',
                                validators=[validators.FileExtensionValidator(
                                    allowed_extensions=('txt', 'doc', 'docx', 'text', 'log'))],
                                error_messages={
                                    'invalid_extension': 'Данный формат файла не поддерживается'
                                })

    class Meta:
        model = SuggestBook

        fields = ('name', 'author', 'text', 'url_book', 'captcha', 'user_book')
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control border"}),
            'author': forms.TextInput(attrs={"class": "form-control border"}),
            'text': forms.TextInput(attrs={"class": "forms-control border"}),
            'url_book': forms.URLInput(attrs={"class": "forms-control border"}),
        }
