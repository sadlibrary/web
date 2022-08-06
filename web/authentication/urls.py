from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.auth_login, name='login'),
    path('logout/', views.auth_logout, name='logout'),
]
