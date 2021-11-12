from django.urls import path
from budget import views

urlpatterns = [
    path('getallfoods/', views.get_all_foods),
    path('addfood', views.user_foods),
]
