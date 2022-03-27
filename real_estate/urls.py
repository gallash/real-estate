from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('register/', views.user_registration, name='user-registration'),
    path('user/', views.user_dashboard, name='user-dashboard'),
    path('renting/', views.rental_request, name='rental-request'), # Como fazer pagination?
    path('house-registration/', views.place_house_registration, name="house-registration")
]
