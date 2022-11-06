from django.urls import path

from .views import *

urlpatterns = [
    path('', BookViews.as_view(), name='book_views')
]
