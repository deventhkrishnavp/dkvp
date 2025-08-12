from django.urls import path
from . import views

urlpatterns = [
    path('vendor_register/', views.vendor_register, name='vendor_register'),
    path('vendor_login/', views.login, name='vendor_login'),
    path('vendor_dashboard/', views.vendor_dashboard, name='vendor_dashboard'),


path('vendor_logout/', views.vendor_logout, name='vendor_logout'),
    ]


