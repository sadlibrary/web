from django.urls import path, include
from library import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'libraries', views.LibraryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
