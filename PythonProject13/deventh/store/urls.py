from django.urls import path,include
from . import views

urlpatterns = [

    path('register/', views.register_views, name='register'),
    path('login/', views.login_views, name='login'),
    path('logout/', views.logout_views, name='register'),
    path('dashboard/', views.dashboard_views, name='dashboard'),

]

