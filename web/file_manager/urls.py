from django.urls import path

from . import views

urlpatterns = [
    # path('test/', views.test, name='file-manager-test'),  An example
    path('login/', views.auth_login, name='file-manager-login'),
    path('home/', views.get_home, name='file-manager-home'),
]