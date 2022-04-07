from django.urls import path
from . import views
from . import forms

urlpatterns = [
    path('all/', views.AuthorListView.as_view(), name="all_authors"),
    path('<int:pk>', views.AuthorDetailView.as_view(), name="author_detail"),
    path('<int:id>/edit/', views.author_form, name="author_form"),
    path('create/', views.author_form, name="author_create")
]
