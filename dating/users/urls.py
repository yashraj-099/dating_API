from django.urls import path
from .views import RegisterView, NearbyUsers

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('nearby-users/', NearbyUsers.as_view(), name='nearby-users'),
]
