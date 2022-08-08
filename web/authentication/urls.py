from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.auth_logout, name='logout'),
]
