from django.urls import path, re_path
from . import views

urlpatterns = [
    path('register/', views.user_registration, name='user-registration'),
    path('user/', views.user_dashboard, name='user-dashboard'),
    path('renting/', views.rental_request, name='rental-request'), # Como fazer pagination?
    path('house-registration/', views.place_house_registration, name="house-registration"),
    path('appartment-registration/', views.place_appartment_registration, name="appartment-registration"),
    path('kitnet-registration/', views.place_kitnet_registration, name="kitnet-registration"),
    path('staff-dashboard', views.staff_dashboard, name="staff-dashboard"),
    path('request-management', views.request_management, name="request-management"),
    # path('request-management/<>', views.request_management, name="request-management"),
    path('view-rented/', views.view_rented, name="view-rented"),
    path('interest/<int:place_id>/', views.rental_request, name="rental-request"),
    # re_path(r'^accept/(?P<place_id>\d+)$', views.accept),
    path('accept/<int:place_id>/', views.accept, name="accept"),
    path('refuse/<int:place_id>/', views.refuse, name="refuse"),
    path('<int:place_id>/', views.pagination, name="pagination"),
    path('', views.main, name="main")
]
