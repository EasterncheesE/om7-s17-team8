from django.urls import path
from . import views
from . import forms

urlpatterns = [
    path('all/', views.CustomUserListView.as_view(), name="all_customusers"),
    path('<int:pk>', views.CustomUserDetailView.as_view(), name="customuser_detail"),
    path('<int:id>/edit/', views.customuser_form, name="customuser_form"),
    path('create/', views.customuser_form, name="customuser_create")
]
