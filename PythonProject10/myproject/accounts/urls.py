
from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.register, name='register'),
    # Registration URL
          # Login URL (optional)
    path('login/', views.loginn, name='login'),
]

