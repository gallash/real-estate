from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_registration, name='user-registration'),
    path('user/', views.user_dashboard, name='user-dashboard'),
    path('renting/', views.rental_request, name='rental-request'), # Como fazer pagination?
    path('house-registration/', views.place_house_registration, name="house-registration"),
    path('appartment-registration/', views.place_appartment_registration, name="appartment-registration"),
    path('kitnet-registration/', views.place_kitnet_registration, name="kitnet-registration"),
    path('interest/<int:place_id>/', views.rental_request, name="rental-request"),
    path('<int:place_id>/', views.pagination, name="pagination"),
    path('', views.main, name="main")
]
