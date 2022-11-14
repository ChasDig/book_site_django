from django import forms

from .models import *


class ReviewsForm(forms.ModelForm):
    """ Форма для добавления отзывов """

    class Meta:

        model = Reviews

        fields = ("name", "email", "text")
