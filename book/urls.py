from django.urls import path
from book import views

urlpatterns = [
    path('all/', views.BookListView.as_view(), name="all_books"),
    path('available/', views.UnorderedBookView.as_view(), name="unordered_books"),
    path('filter/', views.FilterBooksView.as_view(), name="filter_books"),
    path('sorted/', views.SortedBookView.as_view(), name="sorted_books"),
    path('<int:pk>/', views.BookDetailView.as_view(), name="book_detail"),
    path('<int:id>/edit/', views.book_form, name="book_form"),
    path('create/', views.book_form, name="book_create")
]
