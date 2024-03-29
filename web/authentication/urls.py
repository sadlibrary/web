from django.urls import path
from authentication import views


app_name = 'authentication'
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.auth_logout, name='logout'),
    path('profile/', views.view_profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('current_user/', views.current_user, name='current_user'),
    path('change_password/', views.change_password, name='change_password'),
]
