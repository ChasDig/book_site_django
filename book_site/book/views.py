from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class BookViews(ListView):

    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'

    # Create get_context_data:
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        return context

