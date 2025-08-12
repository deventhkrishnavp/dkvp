from django.urls import path
from .import views


urlpatterns=[
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('log', views.log, name='log'),
    path('package', views.all_package, name='all_package'),
    path('package', views.all_package, name='all_package'),
    path('package/top/', views.top_packages, name='top_packages'),


]