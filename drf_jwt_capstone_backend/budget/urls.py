from django.urls import path
from budget import views

urlpatterns = [
    path('getallfoods/', views.get_all_foods),
    path('getuserfoods/', views.user_foods),
    path('addfood/', views.user_foods),
    path('getallexpenses/', views.get_all_expenses),
    path('getuserexpenses/', views.user_expenses),
    path('addexpense/', views.user_expenses),
    path('getallinsurance/', views.get_all_insurances),
    path('getuserinsurance/', views.user_insurances),
    path('addinsurance/', views.user_insurances),
    path('getalltransportation/', views.get_all_transportations),
    path('getusertransportation/', views.user_transportations),
    path('addtransportation/', views.user_transportations),
    path('getallhousing/', views.get_all_houses),
    path('getuserhousing/', views.user_houses),
    path('addhousing/', views.user_houses),
    path('getallutilities/', views.get_all_utility),
    path('getuserutilities/', views.user_utility),
    path('addutilities/', views.user_utility)

]
