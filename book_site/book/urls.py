from django.urls import path, include
from django.views.decorators.cache import cache_page


from .views import *

urlpatterns = [
    path('', BookViews.as_view(), name='book_views'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('filter/', FilterBookViews.as_view(), name='filter_views'),
    path("search/", SearchBook.as_view(), name='search_book'),
    path('suggest_book/', SuggestBookViews.as_view(), name='suggest_book'),
    path('social/', include('social_django.urls', namespace='social')),
    path('<slug:slug>/', BookOneDataViews.as_view(), name='book_one_views'),
    path('category/<slug:slug>/', CategoryViews.as_view(), name='category_views'),
    path('author/<slug:slug>/', AuthorDataViews.as_view(), name='author_one_views'),
    path('add_work/<int:pk>', ReviewsViews.as_view(), name='add_work_views'),
]
