from django.urls import path, include
from library import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'libraries', views.LibraryViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('add-type', views.add_library_type),
    path('add-library', views.add_library),
    path('delete-library', views.delete_library),
    path('', views.library_home),
]
