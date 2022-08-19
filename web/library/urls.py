from django.urls import path
from library import views

urlpatterns = [
    path('file/', views.get_file, name='file'),
]
