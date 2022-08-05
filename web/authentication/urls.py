from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.authenticate, name='authenticate'),
]
