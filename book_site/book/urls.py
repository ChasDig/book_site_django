from django.urls import path


from .views import *

urlpatterns = [
    path('', BookViews.as_view(), name='book_views'),
    path('filter/', FilterBookViews.as_view(), name='filter_views'),
    path('<slug:slug>/', BookOneDataViews.as_view(), name='book_one_views'),
    path('category/<slug:slug>/', CategoryViews.as_view(), name='category_views'),
    path('author/<slug:slug>/', AuthorDataViews.as_view(), name='author_one_views'),
    path('add_work/<int:pk>', ReviewsViews.as_view(), name='add_work_views'),
    path("search/", SearchBook.as_view(), name='search_book'),
]
